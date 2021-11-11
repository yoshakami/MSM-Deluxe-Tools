from tkinter import Tk, Label, Button, END, Entry, StringVar, OptionMenu, Checkbutton, font
from tkinter.filedialog import askdirectory
from functools import partial
import webbrowser
import struct
import os

# thanks to this article : http://wiki.tockdom.com/wiki/THP_(File_Format)
# though it doesn't talk about OffsetsDataOffset, either it's zero and the file format documents everything
# or it's an offset to the start of a table containing UInt32 of cumulated frame data size, generally the offset is 0x60
# the length of that table is the number of frame multiplied by 4. the last value is equal to 0x1C	UInt32	Length of all frames.
# why not pasting the whole documentation here with my knowledge added :)
# Offset	Type	Description
# 0x00	String	File magic. Always THP. in ASCII (0x54485000).
# 0x04	UInt32	Version number. Mario Kart Wii uses 0x11000.
# 0x08	UInt32	Max buffer size.
# 0x0C	UInt32	Max audio samples.
# 0x10	Float	Frames per second.
# 0x14	UInt32	Number of frames in this file.
# 0x18	UInt32	Length of the first frame.
# 0x1C	UInt32	Length of all frames.
# 0x20	UInt32	Offset to components.
# 0x24	UInt32	OffsetsDataOffset. if it isn't equals to 0, it's normally 0x60, the offset to the start of a table
# 0x28	UInt32	First frame offset.
# 0x2C	UInt32	Last frame offset.
#
# Component structure  -  generally starts at 0x30, I've never seen it at another offset
# Offset	Type	Description
# 0x00	UInt32	Number of components.
# 0x04	SByte[16]	Component types (0 = video, 1 = audio, -1 = none).
#
# Video  -  should be starting at offset 0x44 normally
# Offset	Type	Description
# 0x00	UInt32	Width.
# 0x04	UInt32	Height.
# 0x08	UInt32	Video format (only used in version 0x11000).
#
# Audio  -  should be starting at offset 0x50 normally or it's not existing if there's no audio in the file
# Offset	Type	Description
# 0x00	UInt32	A = Number of audio channels.
# 0x04	UInt32	Frequentie.
# 0x08	UInt32	Number of samples.
# 0x0C	UInt32	Number of datas (only used in version 0x11000).
#
# Table OffsetsData  -  exists only if OffsetsDataOffset is not null  -  should be starting at offset 0x60 normally
# Offset	Type	                Description
# 0x00	UInt32[Number of frames]    Cumulated frame data size.
#
# Frame   -   either starts at offset 0x60 or depends of the above table length or wether there's audio or not
# Offset	Type	Description
# 0x00	UInt32	Next total size.
# 0x04	UInt32	Previous total size.
# 0x08	UInt32	I = Image size.
# 0x0C	UInt32	M = Audio size (only exist if the frame contains audio).
# 0x0C or 0x10	Image data  -  apparently it's called "motion jpeg"
#
# Video
# Video data.
#
# Offset	Type	Description
# 0x00	Byte[I]	Image data.
# I	End of image data
# Audio
# Audio data.  -  apparently it's ADPCM audio
#
# Offset	Type	Description
# 0x00	UInt32	Channel size.
# 0x04	UInt32	Number of samples.
# 0x08	Int16[16]	Table 1.
# 0x28	Int16[16]	Table 2.
# 0x48	Int16	Channel 1 previous 1.
# 0x4A	Int16	Channel 1 previous 2.
# 0x4C	Int16	Channel 2 previous 1.
# 0x4E	Int16	Channel 2 previous 2.
# 0x50	Audio Data
# Offset	Type	Description
# 0x00	Byte[M]	Audio data.
# M	End of audio data

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[23])
msm = int(language[1].split(":")[1])
button_row = []
for j in range(11, 20):
    button_row += [j, j, j]
for _ in range(4):
    for j in range(11, 20):
        button_row += [j]
for j in range(20, 32):
    button_row += [j, j, j, j, j, j, j]

print(f"{language[start + 2]}\n")
button_col = [0, 1, 2] * 9 + [3] * 9 + [4] * 9 + [5] * 9 + [6] * 9 + [0, 1, 2, 3, 4, 5, 6] * 12
print(button_col)
button_list = []
a = Tk()
a.title(language[start])
a.minsize(660, 440)
a.config(bg='#eda187')
a.iconbitmap('C:\\Yosh\\msm_stuff\\thp.ico')
japanese = font.Font(size=11)  # (family='MS UI Gothic', size=14) no longer japanses as "japanese emotes are childish"
m = font.Font(family='MARIO Font v3 Solid', size=20)  # , weight='bold')


def first_frame(file, overwrite):
    new_data = b''
    with open(file, 'rb') as thp:
        new_data += thp.read(0x14) + b'\x00\x00\x00\x01'
        thp.seek(0x18)
        frame_length = thp.read(4)
        thp.seek(0x20)
        byte = thp.read(4)  # normally b'\x00\x00\x00\x30'
        component_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
        offsets_data_offset = thp.read(4)
        new_data += frame_length * 2 + byte + offsets_data_offset
        byte = thp.read(4)
        first_frame_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
        thp.seek(0x30)  # new data contains every value of the new header from 0x00 to 0x28 (missing first frame offset)
        if component_offset != 0x30:
            print(f'I WANT THAT THP FILE -> {file}')

        if offsets_data_offset != b'\x00\x00\x00\x00':

            byte = offsets_data_offset
            table = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]
            new_first_frame_offset = table + 4
            new_data += (new_first_frame_offset.to_bytes(4, "big")) * 2 + thp.read(table + 4 - 0x30)  # now it just needs to add all left frames

        else:  # offsets_data_offset isn't in the file.
            new_data += byte * 2  # first frame offset and last frame offset are the same lol
            thp.seek(component_offset)
            new_data += thp.read(first_frame_offset - component_offset)

        thp.seek(first_frame_offset)  # the one in the file, not the new one
        byte = frame_length
        first_frame_length = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
        new_data += thp.read(first_frame_length)  # reads the new total length, not all frames

    if overwrite == b'1' and new_data != b'':
        with open(file, 'wb') as thp:
            thp.write(new_data)
    elif new_data != b'':  # creates a new file the script makes sure it doesn't exists
        n = '-0'
        while os.path.exists(os.path.splitext(file)[0] + n + '.thp'):
            n = '-' + str(int(n[1:]) + 1)
        with open(os.path.splitext(file)[0] + n + '.thp', 'wb') as thp:
            thp.write(new_data)
    return language[start + 3]


def first_frame_vanilla_length(file, overwrite):
    new_data = b''
    with open(file, 'rb') as thp:
        new_data += thp.read(0x10)
        fps = thp.read(4)
        byte = thp.read(4)
        vanilla_frames_number = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
        duration = vanilla_frames_number / (struct.unpack('!f', fps)[0])
        fps = 1 / duration  # literally, the formula is "duration * fps = frame count", so frame count / duration = fps
        thp.seek(0x18)
        frame_length = thp.read(4)
        thp.seek(0x20)
        byte = thp.read(4)  # normally b'\x00\x00\x00\x30'
        component_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
        offsets_data_offset = thp.read(4)
        new_data += hex_float(fps) + b'\x00\x00\x00\x01' + frame_length * 2 + byte + offsets_data_offset
        byte = thp.read(4)
        first_frame_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
        thp.seek(0x30)  # new data contains every value of the new header from 0x00 to 0x28 (missing first frame offset)
        if component_offset != 0x30:
            print(f'I WANT THAT THP FILE -> {file}')

        if offsets_data_offset != b'\x00\x00\x00\x00':

            byte = offsets_data_offset
            table = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]
            new_first_frame_offset = table + 4
            new_data += (new_first_frame_offset.to_bytes(4, "big")) * 2 + thp.read(table + 4 - 0x30)  # now it just needs to add all left frames

        else:  # offsets_data_offset isn't in the file.
            new_data += byte * 2  # first frame offset and last frame offset are the same lol
            thp.seek(component_offset)
            new_data += thp.read(first_frame_offset - component_offset)

        thp.seek(first_frame_offset)  # the one in the file, not the new one
        byte = frame_length
        first_frame_length = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
        new_data += thp.read(first_frame_length)  # reads the new total length, not all frames

    if overwrite == b'1' and new_data != b'':
        with open(file, 'wb') as thp:
            thp.write(new_data)
    elif new_data != b'':  # creates a new file the script makes sure it doesn't exists
        n = '-0'
        while os.path.exists(os.path.splitext(file)[0] + n + '.thp'):
            n = '-' + str(int(n[1:]) + 1)
        with open(os.path.splitext(file)[0] + n + '.thp', 'wb') as thp:
            thp.write(new_data)
    return language[start + 3]


def first_frame_vanilla_length_and_sound_channels(file, overwrite):
    return language[start + 4]


def add_offsets_data_offset(file, overwrite):
    new_data = b''
    with open(file, 'rb') as thp:
        thp.seek(0x24)
        if thp.read(4) != b'\x00\x00\x00\x00':
            return language[start + 5]
        thp.seek(0x14)
        byte = thp.read(4)  # UInt32	Number of frames in this file.
        frame_count = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
        byte = thp.read(4)  # UInt32	Next total size. (here it's the first frame total size)
        frame_size = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
        thp.seek(0x28)
        first_offset = byte = thp.read(4)  # UInt32	First frame offset.
        first_frame_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
        byte = thp.read(4)  # UInt32	Last frame offset.
        last_frame_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
        thp.seek(0)
        new_data += thp.read(0x24) + first_offset + (first_frame_offset + (frame_count * 4)).to_bytes(4, "big")
        new_data += (last_frame_offset + (frame_count * 4)).to_bytes(4, "big")
        thp.seek(0x30)
        new_data += thp.read(abs(first_frame_offset - 0x30))
        # changed header, now the script needs to generate that table which contains UInt32 of cumulated frame data size
        # thp.seek(last_frame_offset)
        # works, but it's probably faster to read the integer at the offset 0x18 so I moved it a few lines above
        thp.seek(first_frame_offset)
        total_size = 0
        while frame_count > 0:
            previous_size = frame_size
            # print(frame_count, first_frame_offset + total_size)
            thp.seek(first_frame_offset + total_size)
            byte = thp.read(4)  # UInt32	Next frame total size.
            frame_size = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
            total_size += previous_size
            new_data += total_size.to_bytes(4, "big")
            frame_count -= 1
        # new_data = new_data
        thp.seek(first_frame_offset)
        new_data += thp.read()

    if overwrite == b'1':
        with open(file, 'wb') as thp:
            thp.write(new_data)
    else:  # creates a new file the script makes sure it doesn't exists
        n = '-0'
        while os.path.exists(os.path.splitext(file)[0] + n + '.thp'):
            n = '-' + str(int(n[1:]) + 1)
        with open(os.path.splitext(file)[0] + n + '.thp', 'wb') as thp:
            thp.write(new_data)
    return language[start + 3]


def remove_offsets_data_offset(file, overwrite):
    new_data = b''
    with open(file, 'rb') as thp:
        thp.seek(0x24)
        byte = new_first_frame_offset = thp.read(4)
        if byte == b'\x00\x00\x00\x00':
            return language[start + 4]
        offsets_data_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
        thp.seek(0x28)
        byte = thp.read(4)  # UInt32	First frame offset.
        first_frame_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
        byte = thp.read(4)  # UInt32	Last frame offset.
        last_frame_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
        difference = first_frame_offset - offsets_data_offset
        thp.seek(0)
        new_data += thp.read(0x24) + b'\x00\x00\x00\x00' + new_first_frame_offset
        # print(difference)
        thp.seek(0x30)
        new_data += (last_frame_offset - difference).to_bytes(4, "big") + thp.read(abs(offsets_data_offset - 0x30))
        thp.seek(first_frame_offset)
        new_data += thp.read()

    if overwrite == b'1':
        with open(file, 'wb') as thp:
            thp.write(new_data)
    else:  # creates a new file the script makes sure it doesn't exists
        n = '-0'
        while os.path.exists(os.path.splitext(file)[0] + n + '.thp'):
            n = '-' + str(int(n[1:]) + 1)
        with open(os.path.splitext(file)[0] + n + '.thp', 'wb') as thp:
            thp.write(new_data)
    return language[start + 3]


def hex_float(number):
    number = number.replace(',', '.')  # replaces coma with dots
    num = b''
    w = hex(struct.unpack('<I', struct.pack('<f', float(number)))[0])[2:]
    # add zeros to always make the value length to 8
    # w = '0' * (8-len(w)) + w
    w = w.zfill(8)
    for octet in range(0, 8, 2):  # transform for example "3f800000" to b'\x3f\x80\x00\x00'
        num += bytes(chr(int(w[octet:(octet + 2)], 16)), 'latin-1')
    return num


def entry_values(file, overwrite):
    frames = entries[3].get()
    new_data = b''
    three_valu = b''
    with open(file, 'r+b') as thp:
        for n in range(3):
            if entries[n].get() == '':  # if it's empty, let the vanilla value
                thp.seek(n * 4 + 8)
                three_valu += thp.read(4)
            else:  # else, add the custom value
                try:
                    if n == 2:
                        three_valu += hex_float(entries[2].get())
                    else:
                        three_valu += int(entries[n].get()).to_bytes(4, "big")
                except ValueError or OverflowError as error:  # it's not an integer or negative for the 2 first settings
                    print(error)
                    return language[start + 7]
        try:
            int(abs(frames)).to_bytes(4, "big")  # checks if the entry is valid
            frames = int(frames)
        except ValueError or OverflowError as error:
            print(error)
            return language[start + 7]
        thp.seek(0x14)
        byte = thp.read(4)  # UInt32	Number of frames in this file.
        frame_count = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
        if frame_count < frames:
            return language[start + 6]
        if frame_count == frames and overwrite:
            thp.seek(8)
            thp.write(three_valu)
        elif frame_count == frames:
            thp.seek(0)
            new_data += thp.read(8) + three_valu
            thp.seek(0x14)
            new_data += thp.read()
        else:  # user decided to reduce the number of frames
            thp.seek(0)
            new_data += thp.read(8) + three_valu + frames.to_bytes(4, "big")
            thp.seek(0x20)
            byte = component = thp.read(4)  # normally b'\x00\x00\x00\x30'
            component_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
            offsets_data_offset = thp.read(4)
            thp.seek(0x28)
            byte = thp.read(4)
            first_frame_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
            thp.seek(0x30)
            if component_offset != 0x30:
                print(f'I WANT THAT THP FILE -> {file}')

            if frames == 0:
                new_data += b'\x00' * 8 + component + b'\x00' * 0x0C
                # new_data += thp.read(component_offset - 0x30)  # it shouldn't change as component offset should be 0x30
                new_data += b'\x00' * 4 + b'\xff' * 16 + b'\x00' * 0x1C
                # new_data += thp.read(first_frame_offset - component_offset - 0x30)  # not zero because OffsetsDataOffset

            elif frames < 0:
                new_data += b'\xff' * 8 + component + b'\xff' * 0x0C
                # new_data += thp.read(component_offset - 0x30)  # it shouldn't change as component offset should be 0x30
                new_data += b'\x00' * 4 + b'\xff' * 24 + b'\x00' * 0x14
                # new_data += thp.read(first_frame_offset - component_offset - 0x30)  # not zero because OffsetsDataOffset

            elif offsets_data_offset != b'\x00\x00\x00\x00':
                thp.seek(0x18)  # UInt32	Length of the first frame.
                new_data += thp.read(4)
                byte = offsets_data_offset
                table = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]
                if frames != 1:
                    thp.seek(table + (frames * 4) - 8)
                    byte = thp.read(4)
                    last_frame_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3] + (table + (frames * 4))
                else:
                    last_frame_offset = first_frame_offset
                    thp.seek(table)
                byte = thp.read(4)
                total_length = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3] + (table + (frames * 4))
                new_data += byte  # UInt32	Length of all frames.
                thp.seek(0x20)
                new_data += thp.read(8) + (table + (frames * 4) - 4).to_bytes(4, "big")
                new_data += last_frame_offset.to_bytes(4, "big")
                thp.seek(0x30)
                new_data += thp.read(table + (frames * 4) - 0x30)  # now it just needs to add all left frames
                thp.seek(first_frame_offset)  # the one in the file, not the new one
                new_data += thp.read(total_length)  # reads the new total length, not all frames

            else:
                thp.seek(0x18)  # UInt32	Length of the first frame.
                frame_length = thp.read(4)
                new_data += frame_length
                # can't build header info without going through the whole file
                # 0x1C	UInt32	Length of all frames. - will need to be taken by going through all frames header
                # 0x20	UInt32	Offset to components. - I hope it's always 0x30, but if it's not, please contact me
                # 0x24	UInt32	OffsetsDataOffset. - b'\x00\x00\x00\x00' as it's literally the condition to trigger here
                # 0x28	UInt32	First frame offset.- doesn't change here
                # 0x2C	UInt32	Last frame offset. - relative to the entry "Total frame count"
                data = b''
                total_size = 0
                while frames > 0:
                    previous_size = frame_size
                    thp.seek(first_frame_offset + total_size)
                    if frames == 1:
                        last_frame_offset = (first_frame_offset + total_size).to_bytes(4, "big")
                    byte = thp.read(4)  # UInt32	Next frame total size.
                    frame_size = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
                    total_size += previous_size
                    frames -= 1
                new_data += total_size.to_bytes(4, "big")  # Length of all frames
                thp.seek(0x20)
                new_data += thp.read(0x0C) + last_frame_offset
                thp.seek(0x30)
                new_data += thp.read(first_frame_offset - 0x30 + total_size)
    if overwrite == b'1' and new_data != b'':
        with open(file, 'wb') as thp:
            thp.write(new_data)
    elif new_data != b'':  # creates a new file the script makes sure it doesn't exists
        n = '-0'
        while os.path.exists(os.path.splitext(file)[0] + n + '.thp'):
            n = '-' + str(int(n[1:]) + 1)
        with open(os.path.splitext(file)[0] + n + '.thp', 'wb') as thp:
            thp.write(new_data)
    return language[start + 3]


def display_info(file, overwrite):
    for previous_info in info_label:
        previous_info.destroy()
    with open(file, 'rb') as thp:
        for k in range(4):
            thp.seek(k * 4 + 8)
            byte = thp.read(4)
            if k == 2:  # frames par second (float)
                info = fps = struct.unpack('!f', byte)[0]
            else:
                info = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
            entries[k].delete(0, 'end')
            entries[k].insert(0, str(info))
        duration = info / fps

        thp.seek(4)  # shows the version. I'm looking for thp with a version different from 00 01 10 00
        byte = thp.read(4)
        version = hex((byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3])[2:].zfill(8)
        content = " ".join(version[k:k + 2] for k in range(0, len(version), 2))
        lversion = Label(a, text=language[start + 17] + content, bg='#eda187')
        lversion.grid(row=5, column=2)

        thp.seek(0x20)
        byte = thp.read(4)  # normally b'\x00\x00\x00\x30'
        offsets_data_offset = thp.read(4)
        component_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
        thp.seek(component_offset + 4)
        result = language[start + 18] + language[start + 16]
        audio = False
        while byte != b'\xff':  # checks if the thp has audio
            byte = thp.read(1)
            if byte == b'\x01':
                audio = True
                result = language[start + 18] + language[start + 15]
        laudio = Label(a, text=result, bg='#eda187')
        laudio.grid(row=6, column=2)

        thp.seek(component_offset + 0x14)  # displays width x height
        byte = thp.read(4)
        width = str((byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3])  # 4 bytes integer
        byte = thp.read(4)
        height = str((byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3])  # 4 bytes integer
        ldim = Label(a, text=language[start + 19].replace('#', width).replace('%', height), bg='#eda187')
        ldim.grid(row=7, column=2)

        result = language[start + 20] + language[start + 16]  # displays wether OffsetsDataOffset is there or not
        if offsets_data_offset != b'\x00\x00\x00\x00':
            result = language[start + 20] + language[start + 15]
        ltable = Label(a, text=result, bg='#eda187')
        ltable.grid(row=8, column=2)

        content = language[start + 24].replace('#', str(duration // 60)).replace('%', str(duration % 60))
        #else:
        #    time = language[start + 24].split('#')
        #    content = time[0] + str(duration) + time[-1]

        lduration = Label(a, text=content, bg='#eda187')
        lduration.grid(row=9, column=0, columnspan=2)

        info_label.append(lversion)
        info_label.append(laudio)
        info_label.append(ldim)
        info_label.append(ltable)
        info_label.append(lduration)
        if audio:
            thp.seek(component_offset + 0x20)
            byte = thp.read(4)
            value = str((byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3])  # 4 bytes integer
            channels = Label(a, text=language[start + 21] + value, bg='#eda187', width=30)
            channels.grid(row=10, column=0)
            byte = thp.read(4)
            value = str((byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3])  # 4 bytes integer
            frequency = Label(a, text=language[start + 22] + value, bg='#eda187', width=30)
            frequency.grid(row=10, column=1)
            byte = thp.read(4)
            value = str((byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3])  # 4 bytes integer
            samples = Label(a, text=language[start + 23] + value, bg='#eda187', width=30)
            samples.grid(row=10, column=2)
            info_label.append(channels)
            info_label.append(frequency)
            info_label.append(samples)
            #for p in range(3):  # Number of audio channels.  Frequentie.  Number of samples.
            #    byte = thp.read(4)
            #    value = str((byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3])  # 4 bytes integer
            #    channels = Label(a, text=language[start + 21 + p] + value, bg='#eda187', width=30)
            #    channels.grid(row=9, column=p)
    return language[start + 3]


def parse(file, index):
    function = done = MODE.get()
    if function == language[start + 24]:
        return

    with open('C:\\Yosh\\a', 'rb') as config2:
        config2.seek(17)
        overwrite = config2.read(1)

    for n in range(len(mode)):
        if function == mode[n]:
            done = launch_func[n](file, overwrite)

    button_list[index].destroy()
    patched = Label(a, text=done, font=japanese, bg='#eda187')
    patched.grid(row=button_row[index], column=button_col[index])


def scan_directory():
    del button_list[:]
    k = 0
    for tkstuff in a.winfo_children():
        if tkstuff not in forstuff:
            tkstuff.destroy()

    for files in os.listdir('./'):
        try:
            if not os.path.isfile(files):
                continue
            size = os.path.getsize(files)
            if size < 10 or k >= len(button_col):
                continue
            with open(files, 'rb') as check_file:
                header = check_file.read(4)
                version = check_file.read(4)
                check_file.seek(0x24)
                OffsetsDataOffset = check_file.read(4)
            if header == b'THP\x00':
                unknown_version = False
                patch = partial(parse, files, k)
                compressbu = Button(a, text=files, command=patch, activebackground='#a9ff99', width=30)
                if version != b'\x00\x01\x10\x00':
                    compressbu.config(bg='#ffa3a3')  # red = I WANT THAT FILE ITS SO UNCOMMON
                    unknown_version = True
                if OffsetsDataOffset != b'\x00\x00\x00\x00':
                    if unknown_version:
                        compressbu.config(bg='#fff999')  # yellow = I WANT THAT FILE EVEN MORE
                    else:
                        compressbu.config(bg='#e6ffb3')  # green = OffsetsDataOffset exists
                compressbu.grid(row=button_row[k], column=button_col[k])
                button_list.append(compressbu)
                k += 1

        except PermissionError as error:
            print(error)
            continue

    if k > 50:  # if many thp are found, then it puts the window on fullscreen and create a big exit button
        exitbu2 = Button(a, text=language[msm + 39], command=a.quit, activebackground='#d9ff8c', bg='#d9ff8c',
                         fg='#ff2222', width=58, height=3, font=(None, 15))
        exitbu2.grid(row=0, column=4, rowspan=2, columnspan=3)
        a.attributes('-fullscreen', True)


def change_directory():  # enter button to change directory (take the entry content)
    cwd = entry_dir.get()
    if cwd == '':
        cwd = os.getcwd()
    else:
        cwd_label.configure(text=cwd)
    entry_dir.delete(0, END)
    os.chdir(cwd)
    scan_directory()


def open_explorer():  # change directory with C:\Windows\explorer.exe GUI
    new_cwd = askdirectory(initialdir=os.getcwd())
    os.chdir(new_cwd)
    cwd_label.configure(text=new_cwd)
    scan_directory()


text_label = Label(a, text=language[msm + 18], bg='#eda187', width=30)
text_label.grid(row=0, column=0)

cwd_label = Label(a, text=os.getcwd(), bg='#eda187', width=60, anchor='w')
cwd_label.grid(row=0, column=1, columnspan=3)

entry_dir = Entry(a, width=30)
entry_dir.grid(row=1, column=1)

refreshbu = Button(a, text=language[msm + 40], command=change_directory, activebackground='#ff9999', width=30)
refreshbu.grid(row=1, column=2)

open_explorerbu = Button(a, text=language[msm + 19], command=open_explorer, activebackground='#96c7ff', width=15)
open_explorerbu.grid(row=1, column=0)


def avthp_github():
    webbrowser.open('https://github.com/jackoalan/avthp/releases/')


def toogle():  # each time the checkbutton overwrite is triggered
    with open('C:\\Yosh\\a', 'r+b') as config:
        config.seek(17)
        config2 = config.read(1)
        config.seek(17)
        if config2 == b'1':
            config.write(b'0')
        else:
            config.write(b'1')


avthp = Label(a, text=language[start + 9], bg='#eda187', width=40)
avthp.grid(row=2, column=0, columnspan=3)

avthpbu = Button(a, text=language[start + 10], command=avthp_github, activebackground='#a9ff91', width=20)
avthpbu.grid(row=2, column=2)

overwrite_checkbu = Checkbutton(a, text=language[start + 8], command=toogle, bg="#eda187", width=15)
overwrite_checkbu.grid(row=2, column=0)

title = Label(a, text=language[start + 1], font=m, bg='#eda187')
title.grid(row=3, columnspan=9)

mode = []
for i in range(26, 32):
    mode.append(' ' * (90 - len(language[start + i])) + language[start + i] + ' ' * (90 - len(language[start + i])))

MODE = StringVar()
MODE.set(language[start + 25])
Mode = OptionMenu(a, MODE, *mode)
Mode["menu"].config(bg="#112", fg='#fff')  # (bg="#000000", fg='#ffffff')
Mode.config(width=90)
Mode.grid(row=4, column=0, columnspan=4)
launch_func = (first_frame, first_frame_vanilla_length,
               add_offsets_data_offset, remove_offsets_data_offset, entry_values, display_info)

ltxt = []
for i in range(11, 15):
    ltxt.append(language[start + i])
forstuff = [text_label, cwd_label, entry_dir, refreshbu, open_explorerbu, overwrite_checkbu, title, avthp, avthpbu, Mode]
entries = []
for i in range(4):  # create the 4 labels in ltxt
    text = Label(a, text=ltxt[i], bg='#eda187', width=30)
    text.grid(row=i + 5, column=0)
    forstuff.append(text)
for i in range(4):  # create 4 entries
    entree = Entry(a, width=25)
    entree.grid(row=i + 5, column=1)
    entries.append(entree)
forstuff += entries

info_label = []

with open('C:\\Yosh\\a', 'rb') as config1:
    config1.seek(17)
    checkbu = config1.read(1)
if checkbu == b'1':
    Checkbutton.select(overwrite_checkbu)

scan_directory()
a.mainloop()
