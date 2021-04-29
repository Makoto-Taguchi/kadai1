import csv

input_path = './csv_files/input_file.csv'
output_path = './csv_files/output_file.csv'

with open(input_path, 'r') as f :
  reader = csv.reader(f)
  for source in reader :
    print(source)

# # 検索ソース
# source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
  
    ### ここに検索ロジックを書く
    if word in source:
      print("{}が見つかりました".format(word))
    else:
      print("{}が見つかりませんでした".format(word))
      source.append(word)
      print(source)

if __name__ == "__main__":
    search()

with open(output_path, 'w') as f:
  writer = csv.writer(f)
  writer.writerow(source)