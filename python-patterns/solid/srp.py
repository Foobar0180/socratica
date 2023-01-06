class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # def save_to_file(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()


class JournalRepository:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('Today is the first of August. It is hot, steamy and wet. It is ' +
            'raining. I am tempted to write a poem. But I remember what it ' +
            'said on one rejection slip: After a heavy rainfall, poems ' +
            'titled RAIN pour in from across the nation. -- Sylvia Plath')
j.add_entry('People rush off to meaningless jobs day after day, you see them ' +
            'coughing in the subways at dawn. They squander their souls on ' +
            'things like “rent,” “decent clothes,” “gas and electricity,” ' +
            '“insurance,” behaving like peasants who have just come out of ' +
            'the fields and are so dreadful tickled because they can buy + '
            'baubles and doodads in stores. -- Jack Kerouac')

# print(f'Journal entries:\n{j}')


journal_file = r'journal.txt'

JournalRepository.save_to_file(j, journal_file)
with open(journal_file) as fh:
    print(fh.read())

