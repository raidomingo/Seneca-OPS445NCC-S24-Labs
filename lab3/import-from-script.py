import lab3a
text = lab3a.return_text_value()
print(text)
print(lab3a.return_number_value())
print(type(lab3a.return_number_value()))

import lab3e
print(lab3e.give_list())
# Will print [100, 200, 300, 'six hundred']
lab3e.give_first_item()
# Will print 100
lab3e.give_first_and_last_item()
# Will print [100, 'six hundred']
lab3e.give_second_and_third_item()
# Will print [200, 300]