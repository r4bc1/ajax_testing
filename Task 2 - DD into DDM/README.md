# Convert Decimal Degrees into Degrees Decimal Minutes

## Description

**Написать функцию, которая конвертирует Decimal Degrees (DD) формат координат в Degrees Decimal Minutes (DDM) формат координат.
С помощью pytest написать параметризированный тест, который принимает навход значение в DD формате и ожидаемое значение в DDM формате.**


Пример:

`def test_cordinates(given_dd, expected_ddm)`

### Тест дата для параметризации:

`TEST_DATA_LONGITUDE = [(-180, "180^0W"), 
						(-180.0, "180^0W"), 
						(-13.912, "13^54.72W"), 
						(0, "0^0E"), (180.0, "180^0E"), 
						(180, "180^0E"), 
						(170.0323, "170^1.938E")]
`

-----

## Running

To run the script simply write in bash:
```bash
python3 DD_to_DDM.py
```

Then you'll have to input the Longitude parameter in DD:
```bash
Enter the DD format and get DDM!
```

-----

## How it works

There is only one function that do all the work - `convert(DD)`.
Firstly it converts the input string into the float format to determine it's sign - negative or positive. So we can say in which hemispere it is.
Then we split the string without minus (if it had to be in this number) by '.' and get two parts - integer part and decimal part.
To calculate Degrees Decimal Minutes we take decimal part of our number, multiply it by 60, round it in the correct and proper way and write it to the and of DDM coordinates.

	For example:
		convert(170.0323) -> 170^1.938E

----
## Testing

To test this script you may have pytest installed:
```
pip install pytest
```

And then you just simply run:
```bash
pytest
```

If you want to get more info about testing - use additionaly the `-v` flag.

### What inside test_for_task2

There are testing list of the tuples with DD coordinates and DDM accordingly.
I use `@pytest.mark.parametrize` and a testing list to assert that everything works fine.

