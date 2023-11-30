import time

def simple_progress_bar(current, total, prefix='', length=30, fill='█', print_end='\r'):
    percent = ("{0:.1f}").format(100 * (current / float(total)))
    filled_length = int(length * current // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% Complete', end=print_end)


for i in range(101):
    time.sleep(3)  # Simulate some work
    simple_progress_bar(i, 100, prefix='Progress:', length=50)

print("\nTask completed!")
