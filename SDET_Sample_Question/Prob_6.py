# Amazon Demp Problem 1
# Problem Statement:
# You are working on a monetary transaction system. Every transaction is logged in a list where each log entry is a string in the following format:
#
# php-template
# Copy
# Edit
# "<sender_user_id> <receiver_user_id> <amount>"
# sender_user_id and receiver_user_id are unique identifiers consisting only of digits (strings with up to 9 digits).
#
# amount is a positive integer (you can ignore it for this task).
#
# You are given a list of such transaction logs and an integer threshold. A user is considered active if they appear as a sender or receiver in at least threshold transactions.
#
# Note: If the sender and receiver are the same in a transaction, count it only once.
#
# Input
# An integer n, the number of transaction logs.
#
# n lines, each containing a log string:
# "<sender_user_id> <receiver_user_id> <amount>"
#
# An integer threshold.
#
# 📤 Output
# A list of user IDs (as strings) who are involved in at least threshold transactions.
#
# The output should be sorted in ascending numeric order.
#
# 🔍 Example
# Input:
# 4
# 1 2 50
# 1 7 70
# 1 3 20
# 2 2 17
# 2
# Output:
# ["1", "2"]
import os


def processLogs(logs, threshold):
    count = {}
    lis = []
    for log in logs:
        l = log.split()
        sender, receiver = l[0], l[1]

        # Count sender
        count[sender] = count.get(sender, 0) + 1

        # Count receiver if different from sender
        if sender != receiver:
            count[receiver] = count.get(receiver, 0) + 1

    for k, v in count.items():
        if v >= threshold:
            lis.append(k)

    return sorted(lis, key=int)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    threshold = int(input().strip())

    result = processLogs(logs, threshold)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()