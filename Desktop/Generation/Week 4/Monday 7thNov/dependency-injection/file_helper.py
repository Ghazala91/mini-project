import csv

class FileHelper: 
    def __init__(self) -> None:
        pass

    def get_file_contents(self, fileName):
        csvRows = [] 
        with open(fileName, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                csvRows.append(row)
        
        return csvRows
          
