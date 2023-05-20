class Page:
    def __init__(self, data_person, secret_nums):
        self.data_person = data_person
        self.secret_nums = secret_nums

    def massive_answer(self, numbers):
        massive = []
        for i in numbers:
            massive.append(int(i))
        print('Work massive')
        print(massive)
        return massive

    def guess_numbers(self, secret, actual):
        bulls = 0
        cows = 0

        for i in range(len(secret)):
            for j in range(len(actual)):
                if i == j and secret[i] == actual[j]:
                    bulls += 1
                elif secret[i] == actual[j]:
                    cows += 1
        print(f'Work guess_numbers: bulls - {bulls}, cows - {cows}')
        if bulls == 4:
            result = '<p>Guess 4 numbers. Enter them separated with spaces:</p>' \
                     '<form method="POST" action="/">' \
                     '<input type="text" name="numbers"/>' \
                     '<input type="submit" value="Send"/>' \
                     '</form>' \
                     '<p>You got right!</p>'
            return result
        else:
            result = '<p>Guess 4 numbers. Enter them separated with spaces:</p>' \
                     '<form method="POST" action="/">' \
                     '<input type="text" name="numbers"/>' \
                     '<input type="submit" value="Send"/>' \
                     '</form>' \
                     f'<p>Bulls: {bulls}, Cows: {cows} </p>'
            return result

    def check_person(self):
        if b'numbers' in self.data_person:
            numbers_string = self.data_person.get(b'numbers')[0].decode()
            numbers_list = numbers_string.split()
            print(self.secret_nums)
            print(numbers_string)
            if all(num.isdigit() for num in numbers_list) and len(numbers_list) == 4:
                print('Work')
                result = self.guess_numbers(self.secret_nums, self.massive_answer(numbers_list))
                if result:
                    result_page = result
                    return result_page
                else:
                    result_page = result
                    return result_page
            else:
                result_page = '<p>Guess 4 numbers. Enter them separated with spaces:</p>' \
                              '<form method="POST" action="/">' \
                              '<input type="text" name="numbers"/>' \
                              '<input type="submit" value="Send"/>' \
                              '</form>' \
                              '<p>Error: Input should be 4 numbers and write numbers</p>'
                return result_page
        else:
            result_page = '<p>Guess 4 numbers. Enter them separated with spaces:</p>' \
                          '<form method="POST" action="/">' \
                          '<input type="text" name="numbers"/>' \
                          '<input type="submit" value="Send"/>' \
                          '</form>'
            return result_page
