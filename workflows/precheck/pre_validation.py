import sys

def validate_file_changes(newly_added_files, updated_files, deleted_files, not_to_be_updated):
    print((sys.argv[1]))
    print (type(sys.argv[1]))
    for file in not_to_be_updated:
        if (file in newly_added_files or file in updated_files or file in deleted_files):
            print ("Config files that are not to be updated or updated. Please approve pull requests manually")
            sys.exit(1)

def main():
    try:
        newly_added_files = sys.argv[1].replace('[', '').replace(']', '').split(',')
        newly_added_files = [str(i) for i in newly_added_files if i]
        print(f"Newly added files {newly_added_files}")

        updated_files = sys.argv[2].replace('[', '').replace(']', '').split(',')
        updated_files = [str(i) for i in updated_files if i]
        print(f"Updated files {updated_files}")

        deleted_files = sys.argv[3].replace('[', '').replace(']', '').split(',')
        deleted_files = [str(i) for i in deleted_files if i]
        print(f"Deleted files {deleted_files}")

        not_to_be_updated = sys.argv[4].replace('[', '').replace(']', '').split(',')
        not_to_be_updated = [str(i) for i in not_to_be_updated if i]
        print(f"Deleted files {not_to_be_updated}")
        json_file = validate_file_changes(newly_added_files, updated_files, deleted_files, not_to_be_updated)

    except Exception as e:
        print(f"[Error] The error occurred in reading the input. The error message is {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
