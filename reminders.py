import copy

import data
import key
from data import Reminder

reminders: dict[str, list[Reminder]] = {
    user: copy.deepcopy(data.REMINDERS_DEFAULT_LIST) for user in key.USER_KEYS
}
