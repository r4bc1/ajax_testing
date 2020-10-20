def convert(DD):
    DD = float(DD)
    hemisphere = "W" if DD < 0 else "E"
    integer_part, decimal_part = [i for i in str(abs(DD)).split(".")]
    decimal_part = str(round(float(str(f"0.{decimal_part}")) * 60, 4)).rstrip("0").rstrip(".")
    DDM = f"{integer_part}^{decimal_part}{hemisphere}"
    return DDM


if __name__ == '__main__':
    print(convert(input("Enter the DD format and get DDM!\n")))
