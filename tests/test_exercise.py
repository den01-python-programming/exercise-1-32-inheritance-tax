import pytest
import src.exercise

def test_exercise():
    input_values = ["500000","3","325000","2","625000","6"]
    input_values_stored = ["500000","3","325000","2","625000","6"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert [output[0],output[1],output[2]] == ["Inheritance:","Years since death:","Tax: 56000.0"]
    assert [output[3],output[4],output[5]] == ["Inheritance:","Years since death:","Tax: 0.0"]
    assert [output[6],output[7],output[8]] == ["Inheritance:","Years since death:","Tax: 24000.0"]
