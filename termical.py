import datetime
import json
import argparse

import termical_module
import termical_event
import termical_functions
import termical_exceptions

desc = 'Termical - a terminal-based calendar'
parser = argparse.ArgumentParser(description=desc, prog='termical')
subparsers = parser.add_subparsers()

# Subcommands

parser_display = subparsers.add_parser('display')
parser_display.add_argument('-s', '--startdate', default=None, type=int, nargs='*')
parser_display.add_argument('-e', '--enddate', default=None, nargs='*', type=int)
display_long_help = 'display long version of events - all information'
parser_display.add_argument('-l', '--long', action='store_true',
                            help=display_long_help)
parser_display.set_defaults(action='display')

parser_schedule = subparsers.add_parser('schedule')
parser_schedule.add_argument('event', nargs='*')
parser_schedule.add_argument('-s', '--startdate', default=None, nargs='*', type=int)
parser_schedule.add_argument('-e', '--enddate', nargs='*', type=int)
schedule_note_help = 'add a note to an event'
parser_schedule.add_argument('-n', '--note', nargs='*', help=schedule_note_help)
schedule_location_help = 'add a location to an event'
parser_schedule.add_argument('-l', '--location', nargs='*',
                             help=schedule_location_help)
parser_schedule.set_defaults(action='schedule')

parser_remove = subparsers.add_parser('remove')
parser_remove.add_argument('event', nargs='*')
parser_remove.add_argument('-s', '--startdate', nargs='*', type=int)
parser_remove.add_argument('-e', '--enddate', nargs='*', type=int)
parser_remove.set_defaults(action='remove')

parser_move = subparsers.add_parser('move')
parser_move.add_argument('event')
parser_move.add_argument('-s', '--sourcedate', nargs='*', type=int)
parser_move.add_argument('-e', '--source-end-date', nargs='*', type=int)
parser_move.add_argument('-t', '--target_date', nargs='*', type=int)
move_note_help = "change event's note in the go"
parser_move.add_argument('-n', '--note', nargs='*', help=move_note_help)
move_location_help = "change event's location in the go"
parser_move.add_argument('-l', '--location', nargs='*', help=move_location_help)
parser_move.set_defaults(action='move')

# Options and flags

interactive_help_message = 'change to the interactive mode'
parser.add_argument('-i', '--interactive', help=interactive_help_message,
                    action='store_true')
verbose_help_message = 'make termical verbose'
parser.add_argument('-v', '--verbose', help=verbose_help_message,
                    action='store_true')

args = parser.parse_args()

print(args)


# Logic

if args.interactive:
    start_message = "Welcome to TermiCal, a terminal-based calendar created by"
    start_message += " Czuhajster.\n"
    print(start_message)
    usage_message = "Display schedule for given time interval: d\n"
    usage_message += "Schedule an event: s\n"
    usage_message += "Remove an event: r\n"
    usage_message += "Move (reschedule) an event: m\n"
    usage_message += "Change your server's address: \n"
    usage_message += "Get help: h\n"
    usage_message += "Quit: q"
    print(usage_message)

    while True:
        action = input('\nWhat do you want to do? ')
        if action == 'd':
            specific_start_date = input('Enter specific date(s) (in YYYY MM DD'
                                  ' format)'
                                  '[today]: ')
            if not specific_start_date:
                specific_start_date = 'today'
            elif specific_start_date == 'q':
                break
            else: 
                specific_start_date = specific_start_date.split()
                specific_start_date = list(map(int, specific_start_date))

            specific_end_date = input('Enter specific end date (in YYYY MM DD'
                                      ' format) [today]: ')
            if not specific_end_date:
                specific_end_date = None
            elif specific_end_date == 'q':
                break
            else: 
                specific_end_date = specific_end_date.split()
                specific_end_date = list(map(int, specific_end_date))

            display = termical_functions.display(specific_start_date,
                                                 specific_end_date)
            print(display)
        elif action == 's':
            title = input('Enter the title of the event: ')
            if title == 'q':
                break
            start_date = input('Enter start date of the event (in YYYY MM DD'
                               ' format) [today]: ')
            if not start_date:
                start_date = 'today'
            elif start_date == 'q':
                break
            else: 
                start_date = start_date.split()
                start_date = list(map(int, start_date))
            end_date = input('Enter end date of the event (in YYYY MM DD'
                             ' format) [today]: ')
            if not end_date:
                end_date = None
            elif end_date == 'q':
                break
            else: 
                end_date = end_date.split()
                end_date = list(map(int, end_date))
            note = input("Enter event's note: ")
            if note == 'q':
                break
            location = input("Enter event's location: ")
            if location == 'q':
                break
        elif action == 'r':
            specific_date = input('Enter specific date (in YYYY MM DD format): ')

        elif action == 'm':
            title = input("Enter event's title: ")
            source_start_date = input("Enter event's current start date (in"
                                      " YYYY MM DD format): ")
            if not source_start_date:
                source_start_date = 'today'
            elif source_start_date == 'q':
                break
            else: 
                source_start_date = source_start_date.split()
                source_start_date = list(map(int, source_start_date))

            source_end_date = input("Enter event's current end date (in"
                                    " YYYY MM DD format): ")
            if not source_end_date:
                source_end_date = None
            elif source_end_date == 'q':
                break
            else: 
                source_end_date = source_end_date.split()
                source_end_date = list(map(int, source_end_date))

            target_start_date = input("Enter event's new start date (in YYYY MM DD"
                               " format) [no change]: ")
            if not target_start_date:
                target_start_date = 'today'
            elif target_start_date == 'q':
                break
            else: 
                target_start_date = target_start_date.split()
                target_start_date = list(map(int, target_start_date))

            target_end_date = input("Enetr event's new end date (in YYYY MM DD"
                             " format) [no change]: ")
            if not target_end_date:
                target_end_date = None
            elif target_end_date == 'q':
                break
            else: 
                target_end_date = target_end_date.split()
                target_end_date = list(map(int, target_end_date))

            location = input("Enter event's new location [no change]: ")

            note = input("Enter event's new note [no change]: ")
            

            move = termical_functions.move(title, source_start_date,
                                           source_end_date, target_start_date,
                                           target_end_date, location, note)

        elif action == 'h':
            pass

        elif action == 'q':
            break

elif args.action == 'display':
    start_date = args.startdate
    end_date = args.enddate
    long = args.long
    if end_date:
        display = termical_functions.display(start_date, end_date, long)
    elif not end_date:
        display = termical_functions.display(start_date, long)
    for date, schedule in display.items():
        print(f"\n{date}:")
        if not schedule:
            print("\tNo events for this date.")
        elif schedule:
            for event in schedule.values():
                print(f"\t{event['title']}")
                print(f"\t\ttitle: {event['title']}")
                print(f"\t\tstart date: {event['start date']}")
                if event['end date']:
                    print(f"\t\tend date: {event['end date']}")
                if 'location' in event.keys():
                    print(f"\t\tlocation: {event['location']}")
                if 'note' in event.keys():
                    print(f"\t\tnote: {event['note']}")

elif args.action == 'schedule':
    event = args.event
    start_date = args.startdate
    end_date = args.enddate
    location = args.location
    note = args.note
    schedule = termical_functions.schedule(event, start_date, end_date, location, note)
    print(schedule)

elif args.action == 'remove':
    event = args.event
    start_date = args.startdate
    end_date = args.enddate
    remove = termical_functions.remove(event, start_date, end_date)
    for item in remove:
        print(item)

elif args.action == 'move':
    event = args.event
    source_start_date = args.sourcedate
    source_end_date = args.source_end_date
    target_date = args.target_date
    location = args.location
    note = args.note
    move = termical_functions.move(event, source_start_date=source_start_date,
                                   source_end_date=source_end_date,
                                   target_start_date=target_date,
                                   location=location,
                                   note=note)
    for item in move:
        print(item)
