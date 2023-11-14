import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from urlSafety import checkLink
import re


print("Please wait training the ML model...")
spam=pd.read_csv('spam.csv')
spam=spam.where(pd.notnull(spam),'')

z=spam["Message"]
y=spam["Category"]
cv = CountVectorizer()
features = cv.fit_transform(z)
model=svm.SVC(gamma='scale')
model.fit(features,y)
print("Finished Training the ML model.")
print()
'''test = cv.transform(z)
print("Accuracy:",(model.score(test,y)))
'''
def find_urls(message):
    pattern = r"(https?://)?(www\.)?([a-zA-Z0-9-]+)(\.[a-zA-Z0-9-]+)+([/?].*)?"
    matches = re.findall(pattern, message)
    urls = ["".join(match) for match in matches]
    return urls

def checkSpam(s):
    i=s
    print("Message:")
    print(i)
    print("\nSpam Message : ")
    i=i.lower()
    features_test=cv.transform([i])
    score=model.predict(features_test)[0]
    if score=="ham":
        score="not Spam"
    print("Mostly",score)
    urls=find_urls(s)
    if urls!=[]:
        print("URLs in the Given Message:")
    for url in urls:
        safety=checkLink(url)
        print(url,":",safety)


exSpam=("Join us to earn a chance to get free cash upto Thousand dollars ! You can find the link at youtube.com")
choice=-1
print("Example for spam Message:")
checkSpam(exSpam)

while choice:
    print()
    choice=int(input("0.Quit \n 1.Check Safety of the given URLs \n 2.Check Message Safety\nChoice: "))
    if choice==0:
        break
    elif choice==1:
        n_url=int(input("No of URLs to check:"))
        for _ in range(n_url):
            url=input("Enter Valid URL: ")
            safety=checkLink(url)
            print(url,":",safety)
    elif choice==2:
        message=input("Enter the Message Contents(Can also include links): ")
        checkSpam(message)
    else:
        continue
    
