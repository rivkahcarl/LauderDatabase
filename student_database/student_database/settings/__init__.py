import os

if os.environ.get('LAUDER_PRD') == '1':
    from student_database.settings.prod import *  # noqa
else:
    from student_database.settings.dev import *  # noqa
