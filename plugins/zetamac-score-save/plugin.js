console.log("Loaded score logger")

var config = { childList: true, subtree: true };

var problem = $("span[class='problem']")[0];
var score = $("span[class='correct']")[0];
var time = $("span[class='left']")[0];

var problem_change_callback = function(mutationsList) {
    // problem changed, log?
    // not for now.
};

var time_change_callback = function(mutationsList) {
    var tleft = parseInt(time.innerHTML.split(": ")[1]);
    if (tleft === 0) {
        var curr_score = score.innerHTML.split(": ")[1];
        var req = new XMLHttpRequest();
        req.open("GET", "http://localhost:8015?score="+curr_score)
        req.send()
    }
}

var observer = new MutationObserver(time_change_callback);
observer.observe(time, config);
