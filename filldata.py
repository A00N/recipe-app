

def filldatapsql():
    action = True
    if action:
        with open('Database data/times.txt') as f:
            lines = f.readlines()
            for line in lines:
                sql = "INSERT INTO times (time) VALUES (:time)"
                db.session.execute(sql, {"time": line})
                db.session.commit()

        with open('Database data/categories.txt') as f:
            lines = f.readlines()
            for line in lines:
                sql = "INSERT INTO times (category) VALUES (:category)"
                db.session.execute(sql, {"category": line})
                db.session.commit()

        with open('Database data/prices.txt') as f:
            lines = f.readlines()
            for line in lines:
                sql = "INSERT INTO times (price) VALUES (:price)"
                db.session.execute(sql, {"price": line})
                db.session.commit()
