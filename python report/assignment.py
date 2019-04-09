class Profile:
    array= []
    def setdata (self, name, phone, gender):
        self.name = name
        self.phone = phone
        self.gender = gender
        Profile.array =[self.name, self.phone, self.gender]

a = Profile()
b = []

while True:
    name = input("이름을 입력하세요:")
    if name == "그만":
        for i in  b:
            print("이름은 {}, 전화번호는 {}, 성별은 {}입니다.".format(name,phone,gender))
        break
    phone = input("전화번호를 입력하세요:")
    gender = input("성별을 입력하세요(male 이나 female로 작성해주세요:")
    if(gender != "male" and gender != "female"): gender ="모르겠네용~"
    a.setdata(name, phone, gender)

    b.append(a.array)
    for i in range(len(b)):
        print("이름은 %s, 전화번호는 %s, 성별은 %s입니다." % (b[i][0],b[i][1],b[i][2]))