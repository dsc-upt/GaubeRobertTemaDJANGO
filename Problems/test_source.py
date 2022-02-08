def main(path_in, path_out):
    import os
    from zipfile import ZipFile

    file_name = "source"
    with ZipFile("files" + path_in, 'r') as zip:    
        zip.extractall()

    with ZipFile("files" + path_out, 'r') as zip:    
        zip.extractall()

    os.system(f'g++ files/{file_name}.cpp -o {file_name}.exe')

    if os.path.isfile(f"{file_name}.exe"):
        x = 1
        score = []
        while(1):
            try:
                with open(f"{x}.in") as dest:
                    pass

                os.system(f'{file_name}.exe < {x}.in > output.txt')
    
                with open(f"{x}.out") as test:
                    with open("output.txt") as output:
                        correct = test.read()
                        response = output.read()
                        if response == correct:
                            score.append({"index": x, "value": 1})
                        else:
                            score.append({"index": x, "value": 0})

                os.remove(f"{x}.in")
                os.remove(f"{x}.out")

                x = x + 1
            except:
                break
        os.remove(f"{file_name}.exe")
        return score
    else:
        return [{"index": -1, "value": -1}]