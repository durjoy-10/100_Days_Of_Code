''' time(): Returns the current time in seconds since the epoch as a floating-point number.'''
# import time

# current_time = time.time()
# print("Current time:", current_time)


'''ctime(): Converts a time expressed in seconds since the epoch to a string representing a local time.'''
# import time

# current_time = time.time()
# time_string = time.ctime(current_time)
# print("Current time:", time_string)


'''sleep(): Suspends execution of the calling thread for a specified number of seconds.'''
# import time
# print("Start")
# time.sleep(2)
# print("End")


'''gmtime(): Converts a time expressed in seconds since the epoch to a struct_time in UTC.'''
# import time

# current_time = time.time()
# utc_time = time.gmtime(current_time)
# print("UTC Time:", utc_time)


'''localtime(): Converts a time expressed in seconds since the epoch to a struct_time in local time.'''
# import time

# current_time = time.time()
# local_time = time.localtime(current_time)
# print("Local Time:", local_time)


'''asctime(): Converts a struct_time object to a string representing the time.'''
# import time

# current_time = time.localtime()
# time_string = time.asctime(current_time)
# print("Current Time:", time_string)


'''strftime(): Formats a struct_time object according to a specified format.'''
# import time

# current_time = time.localtime()
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
# print("Formatted Time:", formatted_time)




import time

def main():
    # Get the current time in seconds since the epoch
    current_time = time.time()
    print("Current time in seconds since the epoch:", current_time)

    # Convert the current time to a human-readable format
    current_time_readable = time.ctime(current_time)
    print("Current time in human-readable format:", current_time_readable)

    # Pause the execution of the program for 2 seconds
    print("Pausing for 2 seconds...")
    time.sleep(2)
    print("Resuming execution after 2 seconds.")

    # Measure the time taken by a certain operation
    start_time = time.time()
    # Simulate a time-consuming operation
    for i in range(1000000):
        pass
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Time taken for the operation:", elapsed_time, "seconds")

    # Get the current local time
    local_time = time.localtime()
    print("Local time:", local_time)

    # Get the current UTC time
    utc_time = time.gmtime()
    print("UTC time:", utc_time)

    # Format the current time
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    print("Formatted time:", formatted_time)

    # Parse a string representing a time
    time_string = "2024-04-01 12:00:00"
    parsed_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
    print("Parsed time:", parsed_time)

if __name__ == "__main__":
    main()
