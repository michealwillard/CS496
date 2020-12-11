var request = URLRequest(url: URL(string: "https://hw3api.appspot.com/game")!)
request.httpMethod = "POST"
opp_name
location
date
time
let postString =
request.httpBody = postString.data(using: .utf8)
let task = URLSession.shared.dataTask(with: request) { data, response, error in
    guard let data = data, error == nil else {                                                 // check for fundamental networking error
        print("error=\(error)")
        return
    }

    if let httpStatus = response as? HTTPURLResponse, httpStatus.statusCode != 200 {           // check for http errors
        print("statusCode should be 200, but is \(httpStatus.statusCode)")
        print("response = \(response)")
    }

    let responseString = String(data: data, encoding: .utf8)
    print("responseString = \(responseString)")
}
task.resume()

curl --data-urlencode "opp_name=Rays" --data-urlencode "date=7-30-2016" --data-urlencode "time=6:00 PM" --data-urlencode "location=Bannerwood Park" -H "Accept: application/json" https://hw3api.appspot.com/game
