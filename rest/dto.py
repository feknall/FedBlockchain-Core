
class ModelMetadata:
    modelId = None
    name = None
    clientsPerRound = None
    secretsPerClient = None
    status = None
    trainingRounds = None
    currentRound = None

    def __init__(self, modelId, name, clientsPerRound, secretsPerClient, trainingRounds, status=None, currentRound=None):
        self.modelId = modelId
        self.name = name
        self.clientsPerRound = clientsPerRound
        self.secretsPerClient = secretsPerClient
        self.status = status
        self.trainingRounds = trainingRounds
        self.currentRound = currentRound


    def to_map(self):
        return self.__dict__


class EndRoundModel:
    modelId = None
    round = None
    weights = None

    def __init__(self, modelId, round, weights):
        self.modelId = modelId
        self.round = round
        self.weights = weights

    def to_map(self):
        return self.__dict__


class ModelSecretRequest:
    modelId = None
    weights1 = None
    weights2 = None

    def __init__(self, modelId, weights1=None, weights2=None):
        self.modelId = modelId
        self.weights1 = weights1
        self.weights2 = weights2

    def to_map(self):
        return self.__dict__


class ModelSecretResponse:
    modelId = None
    round = None

    # This if for response
    weights = None

    def __init__(self, modelId, round, weights=None):
        self.modelId = modelId
        self.round = round
        self.weights = weights

    def to_map(self):
        return self.__dict__


class ModelSecretList:
    modelSecretList = None

    def __init__(self, modelSecretList):
        self.modelSecretList = modelSecretList


class CheckInList:
    checkedInTrainers = None

    def __init__(self, checkedInTrainers):
        self.checkedInTrainers = checkedInTrainers


class AggregatedSecret:
    modelId = None
    round = None
    weights = None

    def __init__(self, modelId, round, weights):
        self.modelId = modelId
        self.round = round
        self.weights = weights

    def to_map(self):
        return self.__dict__


class PersonalInfo:
    clientId = None
    username = None
    role = None
    mspId = None
    selectedForRound = None
    checkedIn = None

    def __init__(self, clientId, username, role, mspId, checkedIn, selectedForRound=None):
        self.clientId = clientId
        self.username = username
        self.role = role
        self.selectedForRound = selectedForRound
        self.mspId = mspId
        self.checkedIn = checkedIn

    def to_map(self):
        return self.__dict__


class TrainerMetadata:
    clientId = None
    checkedInTimestamp = None
    roundSelectedFor = None
    username = None

    def __init__(self, clientId, checkedInTimestamp, username, roundSelectedFor):
        self.clientId = clientId
        self.checkedInTimestamp = checkedInTimestamp
        self.username = username
        self.roundSelectedFor = roundSelectedFor
