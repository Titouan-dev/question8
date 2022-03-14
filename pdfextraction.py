from tika import parser

parsed_pdf = parser.from_file("CM2 CM3 VRAI_compressed.pdf")

data = parsed_pdf["content"]
data_lst = parsed_pdf["content"].split("\n\n")
for i in data_lst:
    if len(i) > 100:
        print(i)
        print("___________________________")
        print("___________________________")
