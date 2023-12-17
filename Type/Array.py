from array import array

int_arr = array("i", [1, 2, 3, 4, 5])

arr_buffer = int_arr.buffer_info()

print(f"Array Buffer Info: {arr_buffer}")

int_arr[0] = 10

print(f"Array Buffer Info: {arr_buffer}")
print("-----")

byte_data = b"Hello, World!"

memory_view = memoryview(byte_data)
