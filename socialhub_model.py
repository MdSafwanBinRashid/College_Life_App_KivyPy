class SocialHubModel:
    def __init__(self):
        # Campus events (for calendar)
        self.events = {
            "Career Fair 2026": {
                "date": "Feb 15",
                "title": "Career Fair 2026",
                "location": "RC Cook Union",
                "time": "10:00 AM - 4:00 PM"
            },
            "Basketball Game: University vs State": {
                "date": "Feb 20",
                "title": "Basketball Game: University vs State",
                "location": "Rock Arena",
                "time": "11:00 AM - 1:00 PM"
            },
            "Study Abroad Info Session": {
                "date": "Feb 22",
                "title": "Study Abroad Info Session",
                "location": "International Center",
                "time": "3:00 PM - 5:00 PM"
            },
            "Movie Night: Oppenheimer": {
                "date": "Feb 25",
                "title": "Movie Night: Oppenheimer",
                "location": "Campus Theater",
                "time": "8:00 PM - 11:00 PM"
            }
        }
        
        # Local community events links
        self.event_links = {
            "Downtown Food Festival": "https://www.eventbrite.com/e/downtown-crawfish-jam-2026-tickets-1977394503189?aff=ebdiglgoogleliveevents",
            "Live Music Local Bands Night": "https://www.hubcityhoedown.com/",
            "Farmers Market": "https://www.hattiesburgfarmersmarket.com/",
            "Mardi Gras Parade": "https://www.mardigrasneworleans.com/parades/"
        }
    
    def get_event(self, title):
        return self.events.get(title)
    
    def get_link(self, event_title):
        return self.event_links.get(event_title)