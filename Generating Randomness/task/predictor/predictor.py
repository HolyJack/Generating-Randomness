import random


def preprocess(string):
    return ''.join(c for c in string if c == '0' or c == '1')


def binary_list_gen(length):
    binary_list = []
    if length == 0:
        return [""]
    for i in "01":
        binary_list += ([i + j for j in binary_list_gen(length - 1)])
    return binary_list


def binary_triad_gen():
    new_triad_dict = dict.fromkeys(binary_list_gen(3))
    for triad in new_triad_dict:
        new_triad_dict[triad] = [0, 0]
    return new_triad_dict


def calculate_statistics(triad_dict_f, string):
    for triad in triad_dict_f:
        for i in range(len(string) - 3):
            if string[i:(4 + i)] == triad + "0":
                triad_dict_f[triad][0] += 1
            if string[i:(4 + i)] == triad + "1":
                triad_dict_f[triad][1] += 1


def string_prediction(string, statistics):
    prediction = ""

    for _ in range(3):
        prediction += random.choice("01")
    for i in range(len(new_string) - 3):
        if statistics[string[i:(i + 3)]][0] > statistics[string[i:(i + 3)]][1]:
            prediction += '0'
        elif statistics[string[i:(i + 3)]][0] < statistics[string[i:(i + 3)]][1]:
            prediction += '1'
        else:
            prediction += random.choice("01")
    return prediction


def count_right_symbols(string1, string2):
    right_counter = 0

    for i in range(len(string1) - 3):
        if string1[i + 3] == string2[i + 3]:
            right_counter += 1
    return right_counter


def predict_string(string, statistics):
    predicted_string = string_prediction(string, statistics)
    print("prediction:")
    print(predicted_string)

    right = count_right_symbols(string, predicted_string)
    print("Computer guessed right {} out of {} symbols ({}%)".
          format(right, len(string) - 3, round(right * 100 / (len(string) - 3), 2)))
    calculate_statistics(statistics, string)
    return right


inputs_count = 100
result = ""

print("Please give AI some data to learn...")
while inputs_count - len(result) > 0:
    print("Current data length is {}, {} symbols left".format(len(result), inputs_count - len(result)))
    print("Print a random string containing 0 or 1:")
    new_string = input()
    result += ''.join(i for i in new_string if i == '0' or i == '1')

print("Final data string:")
print(result)

triad_dict = binary_triad_gen()
calculate_statistics(triad_dict, result)

print("""You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!""")
print("Print a random string containing 0 or 1:")
new_string = input()
balance = 1000
while new_string != "enough":
    new_string = preprocess(new_string)
    if len(new_string) >= 3:
        guessed_right = predict_string(new_string, triad_dict)
        balance += len(new_string) - 2 * guessed_right - 3
        print("Your capital is now ${}".format(balance))
    print("Print a random string containing 0 or 1:")
    new_string = input()
print("Game over!")
