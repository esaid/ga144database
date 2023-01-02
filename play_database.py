





node = '500.node'
projet = 'ledpulse'

# values_to_database(dictnodes)


'''
'''
# file_in_lib = glob.glob(f"lib/*.ga") # list fichiers dans /lib
file_in_lib = os.listdir("lib") # list fichiers dans /lib
print(file_in_lib)

# creation et copie fichiers /lib
drive = deta.Drive("simple_drive")
lib = deta.Drive('lib')
# copie des fichiers /lib vers drive
for l in file_in_lib:
    print(l, 'lib/'+l)
    lib.put(l, path='lib/'+l) # file to send, path= local source

# list des fichiers sur drive
result = lib.list()
all_files = result.get("names")
print(result)


print(database.get_file_drive("lib", "delay.ga"))

file = 'logic.ga'
path_destination = 'lib'
path_local = 'lib'
print(f"put the file {file}")
database.put_file_drive(path_destination, file, path_local)  # path destination et pathlocal ont le meme nom

file = 'gpio.ga'
path_destination = "lib"
print(f"delete file  {file}")
database.delete_file_drive(path_destination, file)
print(f"list  {path_destination}  : {database.list_files(path_destination)}")
'''
