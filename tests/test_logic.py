import pytest
from logic import Game_of_life


def test_transformation_data():
    befor = ['4',
             '5 6',
             '******',
             '**X***',
             '***X**',
             '*XXX**',
             '******']
    after_table = [[False, False, False, False, False, False],
                   [False, False, True, False, False, False],
                   [False, False, False, True, False, False],
                   [False, True, True, True, False, False],
                   [False, False, False, False, False, False]]
    after_generation = 4
    after_column = 6
    after_string = 5
    obj = Game_of_life()
    obj.transformation_data(befor)
    assert obj.generation == after_generation
    assert obj.column == after_column
    assert obj.string == after_string
    assert obj.data_table == after_table


@pytest.mark.parametrize("coordinateY,coordinateX,next_state", [(4, 5, True),  # мертва з 3 сусідами
                                                                (2, 4, True),  # мертва з 3 сусідами
                                                                (1, 4, False),  # мертва з 4 сусідами
                                                                (3, 0, False),  # мертва з 2 сусідами
                                                                (1, 5, True),  # жива з 3 сусідами
                                                                (4, 2, True),  # жива з 2 сусідами
                                                                (2, 5, False),  # жива з 1 сусідом
                                                                (0, 2, False)])  # жива з 4 сусідами
def test_next_points_state(coordinateY, coordinateX, next_state):
    obj = Game_of_life()
    obj.data_table = [[True, True, True, False, False, True],
                      [False, True, False, True, False, True],
                      [False, False, False, False, False, True],
                      [False, False, False, False, False, False],
                      [True, False, True, False, False, False]]

    assert obj.next_points_state(coordinateY, coordinateX, obj.data_table) == next_state


def test_next_field_state():
    obj = Game_of_life()
    obj.data_table = [[True, True, True, False, False, True],
                      [False, True, False, True, False, True],
                      [False, False, False, False, False, True],
                      [False, False, False, False, False, False],
                      [True, False, True, False, False, False]]
    next = [[False, False, False, True, True, True],
            [False, True, False, False, False, True],
            [True, False, False, False, True, False],
            [False, False, False, False, False, False],
            [True, False, True, False, False, True]]

    assert obj.next_field_state(obj.data_table) == next

