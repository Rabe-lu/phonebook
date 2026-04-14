class Contact:
    fields = ["last_name", "first_name", "phone", "comment"]

    def __init__(self, contact_id, first_name, last_name, phone, comment):
        self.id = contact_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.comment = comment

    def contact_format(self):
        return f'{self.last_name} {self.first_name}, tel: {self.phone}, //{self.comment}//'

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data.get('id'),
            data.get('first_name', ''),
            data.get('last_name', ''),
            data.get('phone', ''),
            data.get('comment', '')
        )

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'comment': self.comment
        }
