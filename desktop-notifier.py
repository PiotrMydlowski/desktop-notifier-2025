"""
Created 2025
Based on a web tutorial
Author: Piotr M
"""
from win10toast import ToastNotifier
import time


def main():
    """Main function."""
    toaster = ToastNotifier()

    # fetch items
    notifyItems = []
    notifyItems.append(('title', 'description'))
    notifyItems.append(('title2', 'description2'))
    notifyItems.append(('title3', 'description3'))

    for item in notifyItems:
        # update notification data for Notification object
        toaster.show_toast(title=item[0], msg=item[1], duration=2)

        # short delay between notifications
        time.sleep(1)

if __name__ == "__main__":
    main()
