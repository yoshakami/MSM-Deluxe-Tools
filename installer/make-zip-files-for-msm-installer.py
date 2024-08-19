import os
import zipfile
with zipfile.ZipFile("jpg.zip", 'r') as zipf:
    # Get the list of file names in the ZIP archive
    jpg_files = zipf.namelist()

png = ['how-to-run-msm.png', 'MSM Shortcuts.png', 'm.png', 'm2.png', 'm3.png', 'm4.png', 'm5.png', 'm6.png', 'm7.png',
       'm8.png', 'm9.png', 'ma.png', 'mb.png', 'mc.png', 'md.png', 'me.png', 'mf.png', 'mm.png']


common_files = ['n.exe']
exe_files = []
for file in os.listdir('../'):
    
    if os.path.splitext(file)[-1] in ['.py', '.pyw', '.wav', '.txt'] and file != '#language.txt':
        common_files.append(file)
        
    if os.path.splitext(file)[-1] in ['.exe'] and file != 'n.exe':
        exe_files.append(file)

for file in os.listdir('../languages'):
    common_files.append('languages/' + file) 
for file in os.listdir('../msm_stuff'):
    if file not in png: # jpg_files get renamed by the installer
        common_files.append('msm_stuff/' + file)

with zipfile.ZipFile("Common.zip", 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
    # Iterate over the list of files and add them to the ZIP file
    zipf.write('a', 'Yosh\\a')
    for file in common_files:
        # Create the path inside the ZIP file (add 'Yosh/' prefix)
        zip_path = os.path.join("Yosh", file)
        
        # Add the file to the ZIP file with the new path
        zipf.write('../' + file, zip_path)
        
with zipfile.ZipFile("exe.zip", 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
    for file in exe_files:
        # Create the path inside the ZIP file (add 'Yosh/' prefix)
        zip_path = os.path.join("Yosh", os.path.basename(file))
        
        # Add the file to the ZIP file with the new path
        zipf.write('../' + file, zip_path)
print("successfully created Common.zip and exe.zip")
