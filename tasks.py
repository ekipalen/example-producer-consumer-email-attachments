from pathlib import Path
from robocorp import workitems
from robocorp.tasks import get_output_dir, task
from RPA.Excel.Files import Files as Excel


@task
def producer():
    output = get_output_dir() or Path("output")
    excel = Excel()
    # iteration in case there are multiple work items / emails.
    for item in workitems.inputs:
        email = item.email()
        print("Email sent by:", email.from_.address)
        print("Email subject:", email.subject)
        print("Email body:", email.text)

        # read xlsx formatted attachments
        for filename in item.files:
            if ".xlsx" in filename.lower():
                file_path = item.get_file(filename, output / filename)
                excel.open_workbook(file_path)
                rows = excel.read_worksheet_as_table(header=True)
                for row in rows:
                    payload = {
                        "Name": row["Name"],
                        "Zip": row["Zip"],
                        "Product": row["Item"],
                    }
                    workitems.outputs.create(payload)


@task
def consumer():
    """Process all the produced input Work Items from the previous step."""
    for item in workitems.inputs:
        try:
            name = item.payload["Name"]
            zipcode = item.payload["Zip"]
            product = item.payload["Product"]
            print(f"Processing order: {name}, {zipcode}, {product}")
            assert 1000 <= zipcode <= 9999, "Invalid ZIP code"
            item.done()
        except AssertionError as err:
            item.fail("BUSINESS", code="INVALID_ORDER", message=str(err))
        except KeyError as err:
            item.fail("APPLICATION", code="MISSING_FIELD", message=str(err))
