import sqlite3
import models

import sql.base as base

#Player
# KeyError か SQLError

def getStyles():
    query  = "select id from styles"
    return base.executeQuery(query)

