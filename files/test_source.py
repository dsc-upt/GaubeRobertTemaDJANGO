def main():
    import os, sys, io
    from zipfile import ZipFile

    with ZipFile("files/files/test_data_in/in.zip", 'r') as zip:    
        zip.extractall()

    with ZipFile("files/files/test_data_out/out.zip", 'r') as zip:    
        zip.extractall()
    file_name = "source"
    os.system(f'g++ files/{file_name}.cpp -o {file_name}.exe')

    if os.path.isfile(f"{file_name}.exe"):
        x = 1
        while(1):
            try:
                with open(f"{x}.in") as dest:
                    pass

                os.system(f'{file_name}.exe < {x}.in')
                old_stdout = sys.stdout 
                sys.stdout = buffer = io.StringIO()
                sys.stdout = old_stdout 
                whatWasPrinted = buffer.getvalue()
                print(whatWasPrinted)
                os.remove(f"{x}.in")
                os.remove(f"{x}.out")
                x = x + 1
            except:
                break
        os.remove(f"{file_name}.exe")
    else:
        print("Compile not succesfull")