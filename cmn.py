import os
from functools import partial
from tkinter import Tk, Button, Label, Entry
from tkinter.filedialog import askopenfilename, askdirectory

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')

install_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(install_dir, '#language.txt'), 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()
    
n = os.path.join(install_dir, 'n.exe')

arc = int(language[1].split(":")[7])
start = int(language[1].split(":")[15])
msm = int(language[1].split(":")[1])
hashtag = int(language[1].split(":")[3])
cmn = int(language[1].split(":")[33])
a = Tk()
a.title(language[start])
a.minsize(660, 440)
a.config(bg='#dfffaa')
ico = os.path.join('msm_stuff', 'lh.ico')
a.iconbitmap(os.path.join(install_dir, ico))
print(language[cmn + 9])
print(language[cmn + 10])
thrice = [b'U\xaa8-', b'bres', b'\x00 \xaf0', b'\x00\x00\x00\x00']  # arc, brres, tpl and rso files
twice = thrice[:2]
extensions = ['.mdl', '.bin', '.cmp']  # extensions of compressed files recognized
# burow_extract = [6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10] + [6, 7, 8, 9, 10] * 5 + [11] * 8 + [12] * 8 + [13] * 8 + [14] * 8 + [15] * 8 + [16] * 8 + [17] * 8
# bucolumn = [0] + [0, 1, 2] * 5 + [3] * 5 + [4] * 5 + [5] * 5 + [6] * 5 + [7] * 5 + [0, 1, 2, 3, 4, 5, 6, 7] * 7
burow_extract = []
for j in range(6, 11):
    burow_extract += [j, j, j]
for j in range(6, 11):
    burow_extract += [j, j, j, j]
for j in range(11, 18):
    burow_extract += [j, j, j, j, j, j, j]

bucolumn = [0, 1, 2] * 5 + [3, 4, 5, 6] * 5 + [0, 1, 2, 3, 4, 5, 6] * 7

burow_repack = [burow_extract[i] + 16 for i in range(len(burow_extract))]

extract_list = []
repack_list = []
brres_list = ["Coin.brres", "Coin.brres",
              "md_shootcircle01.brres",
              "Coin.brres",
              "CockpitCoin.brres",  # (same as Coin)
              "StarPiece.brres",  # (coin models from st16)
              "IB00.brres",  # (Minishroom ball transformation)
              "IB01.brres",  # (Banana ball transformation)
              "IB02.brres",  # (Bob-Omb ball transformation)
              "IB03.brres",  # (Green Shell ball transformation)
              "IB04.brres",  # (Red Shell ball transformation)
              "IB07.brres",  # (Star ball transformation)
              "IT01_Toadstool.brres",  # (Minishroom item)
              "IT02_Star.brres",
              "IT04_Banana.brres",
              "IT05_Bomb.brres",
              "IT06_GShell.brres",
              "IT07_RShell.brres",
              "qpanel_h.brres",  # (question panel, stop panel from st03 and reverse panel from st09)
              "qpanel_s10.brres", # (question panel from Bowser Jr. Boulevard)
              "Marker.brres",  # (contains 47 models for all languages "P1", "P2"... circle on the ground and star shape)
              "score.brres",  # (3D model of figures)
              "Shadow.brres",
              "wipe.brres"]
brres_len = [0, 0, 0,
             11392,
             38528,
             65664,
             90880,
             134400,
             215168,
             251008,
             290304,
             329600,
             393088,
             453632,
             487424,
             575104,
             664448,
             715904,
             767360,
             950912,
             991360,
             1352832,
             1484800,
             1490048,
             0x193F7F]

##################################################################################
#  TRANSLATION OF MSM BINARY TREE FROM C TO PYTHON 
#  SOURCE 1 : https://wiki.tockdom.com/wiki/BRRES_(File_Format)
#  SOURCE 2 : https://wiki.tockdom.com/wiki/BRRES_Index_Group_(File_Format)
#  Feel free to copy and paste this part into your own file,
#  All functions will not depend on any external variable or file.
##################################################################################
"""The ID of each entry is not a unique number, but is calculated from the name comparing it to another name (see below) and used to search for a given entry. The entries form a binary search tree, with the first entry being the root. The left and right indicies describe this tree.
Calculation of the ID

The ID is calculated by comparing a filename (subject) to an other filename (object) using the following algorithm:

    Find the last non equal character of both names and store the INDEX.
        If the length of the subject filename is greater than the length of the object filename, INDEX is the length of the subject filename minus 1.
        Otherwise compare each pair of characters until a difference is found.
    Now compare both characters of position INDEX and find the highest bit that is not equal. If INDEX exceeds the length of object, assume character value 0. Store the bit index (7 for 0x80 .. 0 for 0x01) as BITNUM.
    Calculate: ID := INDEX << 3 | BITNUM

Initially the subject filename is compared with the the root filename, which is always empty. If an ID with the same value is found while walking through the tree, then a new ID is calculated using the other filename as object. 
"""

def get_highest_bit(val):
    i = 7
    while i > 0 and not (val & 0x80):
        i -= 1
        val <<= 1
    return i


def calc_brres_id (
      object_name,
     object_len,
      subject_name,
     subject_len
):
    if ( object_len < subject_len ):
        return subject_len - 1 << 3 | get_highest_bit(ord(subject_name[subject_len-1]))

    while ( subject_len > 0 ):
    
        subject_len -= 1
        ch = ord(object_name[subject_len]) ^ ord(subject_name[subject_len])
        if (ch):
            return subject_len << 3 | get_highest_bit(ch)
    
    # default case if the root name is empty, for reference point
    return 65535 # ~(u16)0; // this was the C code


"""typedef struct brres_info_t
{
    u16  id;          // id
    u16  left_idx;    // left index
    u16  right_idx;   // right index
    ccp  name;        // pointer to name
    uint nlen;        // lenght of name

} brres_info_t;"""

# Define the structure as a dictionary
def create_brres_info(id, left_idx, right_idx, name, nlen):
    return {
        'id': id,
        'left_idx': left_idx,
        'right_idx': right_idx,
        'name': name,
        'nlen': nlen
    }

def ASSERT(var):
    if not var:
        raise InterruptedError
    
# info: a dictionnary with the C structure above
# id: a 2 bytes integer
def get_brres_id_bit (info, id):
    ASSERT(info) # check that info is not empty
    char_idx = id >> 3
    return char_idx < info["nlen"] and ord(info["name"][char_idx]) >> ( id & 7 ) & 1


def calc_brres_entry(info_list, entry_idx):
    ASSERT(info_list)
    
    # Extract entry
    entry = info_list[entry_idx]
    entry['id'] = calc_brres_id(0, 0, entry['name'], entry['nlen'])
    entry['left_idx'] = entry['right_idx'] = entry_idx
    
    # Previous item
    prev_idx = 0
    prev = info_list[prev_idx]
    
    # Current item
    current_idx = prev['left_idx']
    current = info_list[current_idx] if current_idx < len(info_list) else None
    
    is_right = False
    
    while current and entry['id'] <= current['id'] and current['id'] < prev['id']:
        if entry['id'] == current['id']:
            entry['id'] = calc_brres_id(current['name'], current['nlen'], entry['name'], entry['nlen'])
            if get_brres_id_bit(current, entry['id']):
                entry['left_idx'] = entry_idx
                entry['right_idx'] = current_idx
            else:
                entry['left_idx'] = current_idx
                entry['right_idx'] = entry_idx
        
        prev = current
        is_right = get_brres_id_bit(entry, current['id'])
        current_idx = current['right_idx'] if is_right else current['left_idx']
        current = info_list[current_idx] if current_idx < len(info_list) else None
    
    if current and current['nlen'] == entry['nlen'] and get_brres_id_bit(current, entry['id']):
        entry['right_idx'] = current_idx
    else:
        entry['left_idx'] = current_idx
    
    if is_right:
        prev['right_idx'] = entry_idx
    else:
        prev['left_idx'] = entry_idx


def calc_brres_entries(info_list):
    ASSERT(info_list)
    ASSERT(len(info_list) > 0)
    
    # Setup root entry
    root = info_list[0]
    root['id'] = 0xffff
    root['left_idx'] = root['right_idx'] = 0
    
    for idx in range(len(info_list)):
        calc_brres_entry(info_list, idx)

"""
# Example data for testing
info_list = [
    create_brres_info(id=0, left_idx=0, right_idx=0, name="", nlen=0),  # Root
    create_brres_info(id=0, left_idx=-1, right_idx=-1, name="3DModels(NW4R)", nlen=14),
    create_brres_info(id=0, left_idx=-1, right_idx=-1, name="Textures(NW4R)", nlen=14),
    create_brres_info(id=0, left_idx=-1, right_idx=-1, name="External", nlen=8)
]
calc_brres_entries(info_list)
print(info_list)"""

##################################################################################
#  REWRITE OF WSZST BRRES EXTRACTOR IN PYTHON BY HAND
#  ASSUMPTIONS : all brres are little endian. all ASSERT contents are true
#  SOURCE : me
#  USAGE : extract_brres('cmn_test_DECOMP.brres')
##################################################################################
def extract_brres(brres):
    with open(brres, "rb") as bina:
        data = bina.read(12)
        ASSERT(data[:4] == b'bres') # makes sure the file is a brres
        endian = data[4:6]
        if endian == b'\xfe\xff': # big endian
            # calculating filesize in case another editor added buch of crap after the end of the brres
            filesize = (data[8] << 24) + (data[9] << 16) + (data[10] << 8) + (data[11]) # u32 = 4 bytes unsigned integer
        elif endian == b'\xff\xfe': # little endian -> reversed order
            # calculating filesize in case another editor added buch of crap after the end of the brres
            filesize = (data[8] << 24) + (data[9] << 16) + (data[10] << 8) + (data[11]) # u32 = 4 bytes unsigned integer
        else:
            raise RuntimeError # invalid endian
        data += bina.read(filesize - 12) # read filesize minus what's already read
    # create extracted brres dir
    extracted_dir = os.path.splitext(brres)[0].split('_DECOMP')[0] + "_extracted"
    while os.path.exists(extracted_dir):
        extracted_dir += "_new"
    os.makedirs(extracted_dir)
    
    root_offset = (data[12] << 8) + data[13] # u16 = 2 bytes unsigned short
    sections_number = (data[14] << 8) + data[15] # number of files inside the first brres + 1
    # in cmn_test.bin, there are 1 mdl0 + 2 tex0 + 21 brres + 1 = 0x19 = 25
    
    # parse Brres Index Group 1
    ASSERT(data[root_offset:root_offset + 4] == b'root')
    root_section_size = (data[root_offset + 4] << 24) + (data[root_offset + 5] << 16) + (data[root_offset + 6] << 8) + data[root_offset + 7] # u32
    parse_brres_index_group(data, root_offset + 8, "", extracted_dir) # launch recursive func
    extract_msm_files(data)
    return extracted_dir # return extracted folder name

def calc_int(data, offset, endian):
    if endian == b'\xfe\xff': # big endian
        return (data[offset] << 24) + (data[offset + 1] << 16) + (data[offset + 2] << 8) + data[offset + 3] # u32integer
    elif endian == b'\xff\xfe': # little endian -> reversed order
        return (data[offset + 3] << 24) + (data[offset + 2] << 16) + (data[offset + 1] << 8) + data[offset] # u32integer
    else:
        raise RuntimeError # invalid endian
    
def calc_short(data, offset, endian):
    if endian == b'\xfe\xff': # big endian
        return (data[8] << 24) + (data[9] << 16) + (data[10] << 8) + (data[11]) # u32 = 4 bytes unsigned integer
    elif endian == b'\xff\xfe': # little endian -> reversed order
        return (data[8] << 24) + (data[9] << 16) + (data[10] << 8) + (data[11]) # u32 = 4 bytes unsigned integer
    else:
        raise RuntimeError # invalid endian
    
def extract_brres_sub_file(data, offset, root_name, root_absolute_filepath):
    x = 8
    file_length = 0
    if data[offset + 4:offset + 6] == b'\xFE\xFF':
        file_length = (data[offset + x] << 24) + (data[offset + x + 1] << 16) + (data[offset + x + 2] << 8) + data[offset + x + 3] + offset # u32
    elif data[offset + 4:offset + 6] == b'\xFF\xFE':
        file_length = (data[offset + x + 3] << 24) + (data[offset + x + 2] << 16) + (data[offset + x + 1] << 8) + data[offset + x] + offset # u32
    else:
        print(data[offset + 4:offset + 6], offset, root_name, root_absolute_filepath, data[offset:offset + 32])
        raise InterruptedError # invalid endian bytes
    with open(root_absolute_filepath, 'wb') as sub:
        sub.write(data[offset:offset+file_length])
        
def extract_sub_file(data, offset, root_name, root_absolute_filepath, endian):
    x = 8
    file_length = 0
    if endian == b'\xFE\xFF':
        file_length = (data[offset + x] << 24) + (data[offset + x + 1] << 16) + (data[offset + x + 2] << 8) + data[offset + x + 3] + offset # u32
    elif endian == b'\xFF\xFE':
        file_length = (data[offset + x + 3] << 24) + (data[offset + x + 2] << 16) + (data[offset + x + 1] << 8) + data[offset + x] + offset # u32
    else:
        print(data[offset + 4:offset + 6], offset, root_name, root_absolute_filepath, data[offset:offset + 32])
        raise InterruptedError # invalid endian bytes
    with open(root_absolute_filepath, 'wb') as sub:
        sub.write(data[offset:offset+file_length])

msm_files_offset = []
msm_files_absolute_filepath = []
every_offset_of_a_new_thing = []

def extract_msm_files(data):  # these files have no filesize at offset 8
    every_offset_of_a_new_thing.sort()
    for i in range(len(msm_files_offset)):
        offset = msm_files_offset[i]
        file = msm_files_absolute_filepath[i]
        next_offset = every_offset_of_a_new_thing[every_offset_of_a_new_thing.index(offset) + 1]
        with open(file, 'wb') as administrator:
            administrator.write(data[offset:next_offset])

def parse_brres_index_group(data, offset, root_name, root_folder):
    print(offset, root_name, root_folder)
    print(data[offset: offset + 4])
    if data[offset: offset + 4] in [b'bres']: 
        # root_folder is a file, and not a folder, so I will extract it and quit the function
        extract_brres_sub_file(data, offset, root_name, root_folder)
        return # end of tree
    elif data[offset: offset + 4] in [b'MDL0', b'TEX0', b'SRT0', b'CHR0', b'PAT0', b'CLR0', b'SHP0', b'SCN0', b'PLT0', b'VIS0']:
        # root_folder is a file, and not a folder, so I will extract it and quit the function
        extract_sub_file(data, offset, root_name, root_folder)
        return # end of tree
    if data[offset: offset + 4] in [b'@ARN', b'@FOG', b'@LGT', b'MEI0']: # MSM Special files
        # store file information and extract at the end
        msm_files_offset.append(offset)
        msm_files_absolute_filepath.append(root_folder)
        return # end of tree
    if not os.path.exists(root_folder):
        os.makedirs(root_folder)
        
    brres_index_group_length = (data[offset] << 24) + (data[offset + 1] << 16) + (data[offset + 2] << 8) + data[offset + 3] # u32
    number_of_entries = (data[offset + 4] << 24) + (data[offset + 5] << 16) + (data[offset + 6] << 8) + data[offset + 7] # u32
    print(brres_index_group_length, number_of_entries)
    # parse Brres Index Group 1
    x = 8 + 16 # skip reference point since we're extracting
    ASSERT(data[offset + 8: offset + 12] == b'\xff\xff\x00\x00')
    # info_list = [create_brres_info(id=0, left_idx=0, right_idx=0, name=root_name, nlen=0)]
    # we're extracting!!! no creating the binary tree
    while number_of_entries > 0:
        x += 8 # skip binary tree info
        entry_name_offset = (data[offset + x] << 24) + (data[offset + x + 1] << 16) + (data[offset + x + 2] << 8) + data[offset + x + 3] + offset # u32
        entry_name_offset_len = data[entry_name_offset - 1] # u8
        entry_name = data[entry_name_offset:entry_name_offset + entry_name_offset_len].decode() # converts to str using UTF-8 encoding
        x += 4
        entry_start_offset = (data[offset + x] << 24) + (data[offset + x + 1] << 16) + (data[offset + x + 2] << 8) + data[offset + x + 3] + offset # u32
        every_offset_of_a_new_thing.append(entry_name_offset - 1)
        every_offset_of_a_new_thing.append(entry_start_offset)
        parse_brres_index_group(data, entry_start_offset, entry_name, os.path.join(root_folder, entry_name))
        x += 4
        number_of_entries -= 1
        
##################################################################################
#  REWRITE OF WSZST BRRES CREATOR IN PYTHON BY HAND
#  ASSUMPTIONS : all brres are little endian. all ASSERT contents are true
#  SOURCE : me
#  USAGE : create_brres('cmn_test_DECOMP_new')
##################################################################################

def scan_directory():
    del repack_list[:]
    del extract_list[:]
    for tkstuff in a.winfo_children():
        if tkstuff not in [text_label, cwd_label, entry_dir, refreshbu, open_explorerbu]:
            tkstuff.destroy()

    def repack(cmn_dir):  # compress cfile
        brres_content = b""
        if not os.path.exists(cmn_dir):
            cmn_dir = input("drag and drop cmn_test_extracted in this window then press enter\n")
        if not os.path.exists(brres):
            brres = input("drag and drop cmn_test_DECOMP.bin in this window then press enter\n")
        with open(brres, "r+b") as file:
            for i in range(3, len(brres_list)):
                if not os.path.exists(cmn_dir + "/" + brres_list[i]):
                    print(f"cannot find file, skipping {brres_list[i]}")
                    continue
                file.seek(brres_len[i])
                if brres_len[i] + os.path.getsize(cmn_dir + "/" + brres_list[i]) > brres_len[i + 1]:
                    print(f"{brres_list[i]}'s file size has changed. skipping")
                    continue
                with open(cmn_dir + "/" + brres_list[i], "rb") as brres:
                    brres_content = brres.read()
                file.write(brres_content)
        print(f"rebuilt file!\npress enter to exit...")
        manual_entry.delete(0, 'end')

    def extract(brres):
        data = b''
        with open(brres, "rb") as bina:
            data = bina.read(8)
        if data[:8] != b'bres\xfe\xff\x00\x00': # if it's not a brres
            os.system(f'{n} "{brres}" -x') # convert it to brres
            brres = os.path.splitext(brres)[0] + '_DECOMP.bin'
        print(brres)
        extract_brres(brres)
        """except InterruptedError:
            raise InterruptedError
            print(language[cmn + 11])  # message that it's not a brres
        except FileNotFoundError:
            raise InterruptedError
            print(language[cmn + 11])  # message that it's not a brres"""
        return language[arc + 1]
    
    def explorer_repack():
        repack_dir = askdirectory(initialdir=cwd, title="Select a directory to repack")
        repack(repack_dir)

    def explorer_extract():
        file = askopenfilename(initialdir=cwd)
        try:
            extract_brres(file)
        except InterruptedError:
            print(language[cmn + 11])  # message that it's not a brres
        except FileNotFoundError:
            print(language[cmn + 11])  # message that it's not a brres
        print(language[arc + 1])

    def extract_file(file, number):
        label_text = extract(file)
        extract_list[number].destroy()
        patched = Label(a, text=label_text, bg='#dfffaa', width=30)
        patched.grid(row=burow_extract[number], column=bucolumn[number])

    def repack_file(brres, num):
        repack(brres)
        repack_list[num].destroy()
        patched = Label(a, text=language[arc + 1], bg='#dfffaa', width=30)
        patched.grid(row=burow_extract[num], column=bucolumn[num])

    patched = Label(a, text=language[arc + 1], bg='#dfffaa', width=30)
    patched.grid(row=5, column=0)
    file_extract_label = Label(a, text=language[cmn + 5], font=300, bg='#dfffaa', height=2, width=45)
    file_extract_label.grid(row=2, columnspan=20)

    explorer_extractbu = Button(a, text=language[msm + 19], activebackground='#96c7ff', bg='#c4e0ff', command=explorer_extract, width=87)
    explorer_extractbu.grid(row=5, column=0, columnspan=3)

    p = 0
    for file_to_extract in os.listdir('./'):
        try:
            if os.path.isfile(file_to_extract):
                size = os.path.getsize(file_to_extract)
                if size < 5 or p >= len(bucolumn):
                    continue
                with open(file_to_extract, 'rb') as check_xfile:
                    header = check_xfile.read(4)
                if header[:1] in [b'@', b'\x10', b'\x11', b'\x81', b'\x82', b'$', b'(', b'0', b'P', b'b'] and header != b'PK\x03\x04':  # lh @, old lz \x10, lz77 \x11, diff8 \x81, diff16 \x82, huff4 $, huff8 (, runlength 0, lrc P
                    run_extract_file = partial(extract_file, file_to_extract, p)
                    temp = Button(a, text=file_to_extract, command=run_extract_file, activebackground='#a9ff99', width=30)
                    temp.grid(row=burow_extract[p], column=bucolumn[p])
                    extract_list.append(temp)
                    # print(file_to_extract, p)
                    p += 1

        except PermissionError as error:
            print(error)
            continue

    cmn_repack_label = Label(a, text=language[cmn + 6], font=300, bg='#dfffaa', height=2)
    cmn_repack_label.grid(row=18, columnspan=20)

    manual_explorerbu = Button(a, text=language[msm + 19], command=explorer_repack, activebackground='#ffc773', bg='#ffe4bd', width=87)
    manual_explorerbu.grid(row=21, column=0, columnspan=3)

    manual_label = Label(a, text=language[cmn + 7], bg='#dfffaa', width=30)
    manual_label.grid(row=20, column=0)

    manual_entry = Entry(a, width=30)
    manual_entry.grid(row=20, column=1)

    manual_button = Button(a, text=language[cmn + 8], activebackground='#a9ff91', bg='#c9ffba', width=30)
    manual_repack = partial(repack, manual_entry.get())
    manual_button.config(command=manual_repack)
    manual_button.grid(row=20, column=2)

    i = 0
    for dir_to_repack in os.listdir('./'):
        try:
            if os.path.isdir(dir_to_repack):
                cmn_dir = os.listdir(dir_to_repack)
                this_is_a_cmn_dir = True
                for brres in brres_list:
                    if brres not in cmn_dir:
                        this_is_a_cmn_dir = False
                        break
                if not this_is_a_cmn_dir or i >= len(bucolumn):
                    continue
                run_repack_file = partial(repack_file, dir_to_repack, i)
                temp2 = Button(a, text=dir_to_repack, command=run_repack_file, activebackground='#a9ff91', width=30)
                temp2.grid(row=burow_repack[i], column=bucolumn[i])
                repack_list.append(temp2)
                i += 1

        except PermissionError as error:
            print(error)
            continue
    if i > 50 or p > 50:  # creates a big exit button and make the window fullscreen as it was too tiny to display all buttons
        exitbu2 = Button(a, text=language[msm + 40], command=a.quit, activebackground='#d9ff8c', bg='#d9ff8c', fg='#ff2222', width=58, height=3, font=100)
        exitbu2.grid(row=0, column=4, rowspan=2, columnspan=3)
        a.attributes('-fullscreen', True)


def change_directory():  # enter button to change directory (take the entry content)
    entry_cwd = entry_dir.get()
    if entry_cwd == '':
        entry_cwd = os.getcwd()
    else:
        cwd_label.configure(text=entry_cwd)
    entry_dir.delete(0, 'end')
    os.chdir(entry_cwd)
    scan_directory()


def open_explorer():  # change directory with C:\Windows\explorer.exe GUI
    new_cwd = askdirectory(initialdir=os.getcwd)
    os.chdir(new_cwd)
    cwd_label.configure(text=new_cwd)
    scan_directory()


cwd = os.getcwd()
text_label = Label(a, text=language[msm + 18], bg='#dfffaa', width=30)
text_label.grid(row=0, column=0)
cwd_label = Label(a, text=cwd, bg='#dfffaa', width=60, anchor='w')
cwd_label.grid(row=0, column=1, columnspan=2)
entry_dir = Entry(a, width=30)
entry_dir.grid(row=1, column=1)
refreshbu = Button(a, text=language[msm + 40], command=change_directory, activebackground='#ff9999', width=30)
refreshbu.grid(row=1, column=2)
open_explorerbu = Button(a, text=language[msm + 19], command=open_explorer, activebackground='#96c7ff', width=15)
open_explorerbu.grid(row=1, column=0)
scan_directory()
a.mainloop()
