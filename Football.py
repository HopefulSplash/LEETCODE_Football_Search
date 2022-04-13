import json
import string
import urllib.request

#get the JSON data from online
def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if operUrl.getcode() == 200:
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData


def main():
    teamFind = "manutd"
    totalGoals = 0
    urlData = "https://s3.eu-west-1.amazonaws.com/hackajob-assets1.p.hackajob/challenges/football_session/football.json"
    jsonData = getResponse(urlData)
    #search the data for the team and goals
    for round in range(len(jsonData["rounds"])):
        for item in range(len(jsonData["rounds"][round]["matches"])):
            if jsonData["rounds"][0]["matches"][item]["team1"]["key"] == teamFind:
                totalGoals += jsonData["rounds"][0]["matches"][item]["score1"]

            elif jsonData["rounds"][0]["matches"][item]["team2"]["key"] == teamFind:
                totalGoals += jsonData["rounds"][0]["matches"][item]["score2"]
    print(totalGoals)


if __name__ == '__main__':
    main()
