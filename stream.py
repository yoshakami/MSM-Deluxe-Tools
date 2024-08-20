import shutil
import os

charsound = [[], [], [], [], [], [], [], [], [], [], [], [],
             # characters in slot 0 to 11 use the same file name pattern
             ["VOICE_STRM_C12_126_T2_ST_C14.brstm",
              "VOICE_STRM_C12_130_T2_ST_C14.brstm",
              "VOICE_STRM_C12_20_T1_ST_C14.brstm",
              "VOICE_STRM_C12_127_T2_ST_C14.brstm",
              ],
             ["m_sabo_pu1.brstm",  # pycharm auto formatting, I guess it's how the PEP8 wants scripts to look like
              "m_sabo_s_atk1.brstm",
              "m_sabo_ag2.brstm",
              "m_sabo_id1.brstm"],
             ["VOICE_STRM_C14_251_YES.brstm",
              "VOICE_STRM_C14_246_YES.brstm",
              "VOICE_STRM_C14_256_YES.brstm",
              "VOICE_STRM_C14_252_YES.brstm"],
             ["VOICE_STRM_C15_226_STRM_C14.brstm",
              "VOICE_STRM_C15_170_WIN.brstm",
              "VOICE_STRM_C15_210_STRM_C14.brstm",
              "VOICE_STRM_C15_218_STRM_C14.brstm"],
             ["VOICE_C16_ACTION_S1.brstm",
              "VOICE_C16_ACTION_M1.brstm",
              "VOICE_C16_ACTION_L3.brstm",
              "VOICE_C16_ACTION_M3.brstm"],
             ["VOICE_C17_87_VO_ST_C14.brstm",
              "VOICE_C17_58_STRM_C14.brstm",
              "VOICE_C17_55_STRM_C14.brstm",
              "VOICE_C17_52_STRM_C14.brstm"], []]

for i in range(12):
    charsound[i] = [f"VOICE_STRM_C{str(i).zfill(2)}_00.brstm", f"VOICE_STRM_C{str(i).zfill(2)}_01.brstm",
                    f"VOICE_STRM_C{str(i).zfill(2)}_02.brstm", f"VOICE_STRM_C{str(i).zfill(2)}_03.brstm"]
before_match = """
VOICE_C00_YES.brstm
MARIO_D_DCSUCCESS_01-02.brstm
VOICE_C01_YES.brstm
VOICE_C01_ACTION_L1.brstm
VOICE_C02_YES.brstm
VOICE_C02_ACTION_L3.brstm
ds_org_Select_Chara-01.z.44.brstm
VOICE_C03_ACTION_L2.brstm
VOICE_C03_YES.brstm
VOICE_C03_WIN.brstm
VOICE_C05_YES.brstm
VOICE_C05_ACTION_M2.brstm
VOICE_C06_YES.brstm
VOICE_C06_ACTION_L1.brstm
VOICE_C07_YES.brstm
VOICE_C07_ACTION_M3.brstm
VOICE_C08_YES.brstm
VOICE_C08_ACTION_L1.brstm
VOICE_C09_YES.brstm
VOICE_C09_ACTION_L1.brstm
VOICE_C10_YES.brstm
VOICE_C10_ACTION_L2.brstm
VOICE_C11_YES.brstm
VOICE_C11_ACTION_L2.brstm
VOICE_C12_93_T2_YES.brstm
VOICE_C12_67_T3_L3.brstm
m_sabo_s_atk1.brstm
m_sabo_s_atk2.brstm
VOICE_C14_252_YES.brstm
VOICE_C14_237_T2_L2.brstm
VOICE_C15_94_YES.brstm
VOICE_C15_54_L3.brstm
VOICE_C16_YES.0.brstm
VOICE_C16_ACTION_L2.0.brstm
VOICE_C17_234_YES.0.brstm
VOICE_C17_04_WIN.0.brstm"""
presentation_sound = before_match.splitlines()[1:]

for i in range(18):
    print(presentation_sound[2*i])
    charsound[i].append(presentation_sound[2*i])
    charsound[i].append(presentation_sound[2*i+1])
print(charsound)

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')

install_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(install_dir, '#language.txt'), 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[33])
hashtag = int(language[1].split(":")[3])

stream_path = input(language[start + 2]).strip('"')

source = int(input(f"{language[hashtag + 13].replace('#', os.getcwd)}\n{language[start + 3]} : "))
for sound in charsound[source]:
    shutil.copy2(stream_path + sound, sound)
