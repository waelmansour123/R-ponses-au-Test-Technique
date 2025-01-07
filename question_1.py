def calculate_calibration_sum(file_path):
  try:
    with open(file_path, "r") as file:
        totalsum=0
        for line in file:
            array2 = []
            for i in line:
                if i.isdigit():
                    array2.append(int(i))
            totalsum=totalsum+int(str(array2[0])+str(array2[-1]))

        return totalsum
  except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
  except ValueError as e:
        print(f"Error processing the file: {e}")


if __name__ == "__main__":
    file_path = "document.txt"
    total_sum = calculate_calibration_sum(file_path)
    print(f"Total Calibration Sum: {total_sum}")

