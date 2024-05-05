import sys
from printer import Printer
from validator import Validator
from contact import Contact


printer = Printer()

# printer.logo()
# printer.loading()

validator = Validator(sys.argv)

if validator.error:
    printer.error("Validation error", validator.error)
    sys.exit()

match validator.command:
    case "index":
        printer.verbose("All numbers", Contact.all())
    case "index_limit":
        printer.verbose("All numbers", Contact.all_limit(sys.argv[2], sys.argv[3]))
    case "show":
        if validator.isId(sys.argv[2]):
            contact = Contact.find(sys.argv[2])
        if validator.isNumberP(sys.argv[2]):
            contact = Contact.findByNumber(sys.argv[2][:-1])
        if validator.isNumber(sys.argv[2]):
            contact = Contact.findByNumber(sys.argv[2])
        if validator.isName(sys.argv[2]):
            contact = Contact.findByName(sys.argv[2])
        if not contact:
            printer.error("Not found")
            sys.exit()
        printer.verbose("Number", contact)
    case "add":
        contact = Contact()
        contact.phone = sys.argv[3]
        contact.name = sys.argv[2]
        if not contact.save():
            printer.error("Saving error")
            sys.exit()
        printer.verbose("Successfully added", contact)
    case "edit":
        contact = Contact.find(sys.argv[2])
        if not contact:
            printer.error("Not found")
            sys.exit()

        contact = contact[0]
        contact.name = sys.argv[3]
        contact.phone = sys.argv[4]
        if not contact.update():
            printer.error("Saving error")
            sys.exit()
        printer.verbose("Successfully edited", contact)
    case "delete":
        if validator.isId(sys.argv[2]):
            contact = Contact.find(sys.argv[2])
        if validator.isNumber(sys.argv[2]):
            contact = Contact.findByNumber(sys.argv[2])
        if validator.isName(sys.argv[2]):
            contact = Contact.findByName(sys.argv[2])
        if not contact:
            printer.error("Not found")
            sys.exit()
        contact = contact[0]
        if not contact.destroy():
            printer.error("Deleting error")
            sys.exit()
        printer.verbose("Successfully deleted", contact)
    case "upload":
        with open(sys.argv[2], "r") as file:
            next(file)
            for line in file:
                name, phone = line.strip().split(";")
                contact = Contact()
                contact.phone = phone
                contact.name = name
                contact.save()
        printer.verbose("All numbers", Contact.all())
