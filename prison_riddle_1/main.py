"""
https://www.youtube.com/watch?v=iSNsgj1OCLA&ab_channel=Veritasium

100 prisoners

100 boxes

each prisoner needs to look for the box that contains their number
"""
import random

NUM_PRISONERS = 100
OPEN_BOX_NUM = 50


class Boxes:
    def __init__(self, num_boxes):
        _slip_num_list = random.sample(range(1, num_boxes+1), num_boxes)
        self.boxes = []
        for slip_num in _slip_num_list:
            self.boxes.append(Box(slip_num))

    def get_slip_num(self, box_num):
        """ box_num starts at index 1 """
        return self.boxes[box_num-1].get_slip_num()


class Box:
    def __init__(self, slip_num):
        self.slip_num = slip_num

    def get_slip_num(self):
        return self.slip_num


def main():

    # prisoners = []

    prisoners = random.sample(range(1, NUM_PRISONERS+1), NUM_PRISONERS)

    # boxes = random.sample(range(1, NUM_PRISONERS+1), NUM_PRISONERS)

    boxes = Boxes(NUM_PRISONERS)

    # print(prisoners)
    # print(type(prisoners))
    # print(len(prisoners))

    for prisoner in prisoners:
        # print(index)

        search_box = prisoner

        print(f"prisoner num: {prisoner}")

        for i in range(OPEN_BOX_NUM):
            # prisoner needs to look at the box with their number
            # slip_num = boxes[search_box-1]

            slip_num = boxes.get_slip_num(search_box)

            print(
                f"search_num: {i+1}, box num: {search_box}, slip_num: {slip_num}")

            # then check if it == their number
            if slip_num == prisoner:
                print("Number found, next prisoner")
                break

            search_box = slip_num
            # then go to the next box with the number of the slip in that box in it...

        break


if __name__ == "__main__":
    main()
