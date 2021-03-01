from marshmallow import Schema, fields, EXCLUDE


class RegisterUserSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Str()
    city = fields.Str()
    company = fields.Str()
    country = fields.Str()
    firstName = fields.Str()
    lastName = fields.Str()
    organizationType = fields.Str()
    phone = fields.Str()
    state = fields.Str()
    zipCode = fields.Str()
    disclaimerAccepted = fields.Boolean()
    languageCode = fields.Str()
    emailAddress = fields.Str()


class UnregisterUserSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Str()
    languageCode = fields.Str()
    emailAddress = fields.Str()
    registrationId = fields.Str()
    registrationIdGeneratedTime = fields.Str()


class ProjectMembershipSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Str()
    projectId = fields.Str()
    userId = fields.Str()
