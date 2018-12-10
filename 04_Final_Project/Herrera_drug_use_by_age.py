'''
DrugUseByAge class
'''
class DrugUseByAge:

    def __init__(self, record):
        self.record = record

    def age(self):
        return self.record['age']

    def n(self):
        return self.record['n']

    def alcohol_use(self):
        return self.record['alcohol_use']

    def alcohol_frequency(self):
        return self.record['alcohol_frequency']

    def marijuana_use(self):
        return self.record['marijuana_use']

    def marijuana_frequency(self):
        return self.record['marijuana_frequency']

    def cocaine_use(self):
        return self.record['cocaine_use']

    def cocaine_frequency(self):
        return self.record['cocaine_frequency']

    def crack_use(self):
        return self.record['crack_use']

    def crack_frequency(self):
        return self.record['crack_frequency']

    def heroin_use(self):
        return self.record['heroin_use']

    def heroin_frequency(self):
        return self.record['heroin_frequency']

    def hallucinogen_use(self):
        return self.record['hallucinogen_use']

    def hallucinogen_frequency(self):
        return self.record['hallucinogen_frequency']

    def inhalant_use(self):
        return self.record['inhalant_use']

    def inhalant_frequency(self):
        return self.record['inhalant_frequency']

    def pain_reliever_use(self):
        return self.record['pain_releiver_use']

    def pain_reliever_frequency(self):
        return self.record['pain_releiver_frequency']

    def oxycontin_use(self):
        return self.record['oxycontin_use']

    def oxycontin_frequency(self):
        return self.record['oxycontin_frequency']

    def tranquilizer_use(self):
        return self.record['tranquilizer_use']

    def tranquilizer_frequency(self):
        return self.record['tranquilizer_frequency']

    def stimulant_use(self):
        return self.record['stimulant_use']

    def stimulant_frequency(self):
        return self.record['stimulant_frequency']

    def meth_use(self):
        return self.record['meth_use']

    def meth_frequency(self):
        return self.record['meth_frequency']

    def sedative_use(self):
        return self.record['sedative_use']

    def sedative_frequency(self):
        return self.record['sedative_frequency']

    def display(self):
        result = ""
        for key, value in self.record.items():
            result += str(key) + ": " + str(value) + ", "
        print(result[:-2])

# Method to convert row to record
def row_to_record(row, fields):
    result = {}
    result[fields[0]] = row[0]
    for i in range(1,len(row)):
        result[fields[i]] = format_value(row[i])
    return result

# Method to format header
def format_header(h):
    return h.lower().replace('-','_')

# Method to format value in data
def format_value(v):
    if v == "-":
        return None
    else:
        try:
            return float(v)
        except:
            return v

# Main method for program execution
def main():
    lines = open("drug-use-by-age.csv").readlines()
    header = [format_header(name) for name in lines[0].strip().split(",")]
    rows = [row.strip().split(",") for row in lines[1:]]
    records = []
    for row in rows:
        records.append(row_to_record(row, header))
    objects = []
    for record in records:
        objects.append(DrugUseByAge(record))
    for obj in objects:
        obj.display()
    
    

if __name__ == "__main__":
    main()
