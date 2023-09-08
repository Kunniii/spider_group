from Processor import Processor
from Database import Database

# processor = Processor("./downloads", worker=10)

# processor.run_extract_data()

# processor.load_pickle("data.pkl")

db = Database('./database.sqlite')


db.to_excel('./data.xlsx')
