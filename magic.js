// thanks https://stackoverflow.com/questions/7731778/get-query-string-parameters-with-jquery
function parseQueryString () {
    var parsedParameters = {},
    uriParameters = location.search.substr(1).split('&');

    for (var i = 0; i < uriParameters.length; i++) {
        var parameter = uriParameters[i].split('=');
        parsedParameters[parameter[0]] = decodeURIComponent(parameter[1]);
    }

    return parsedParameters;
}

$(document).ready(function() {
    query_params = parseQueryString();

    if (query_params['status'] == 'LoginError') {
        $('#login_error_message').removeClass('hidden');
    }

    dataset = query_params['dataset'];
    if (dataset == 'Pubmed_JET') {
        $('#dataset').text('JET embeddings');
        $('#inp_dataset').val(dataset);
    }
    else if (dataset == 'UMLS_JET') {
        $('#dataset').text('the UMLS strings file for JET');
        $('#inp_dataset').val(dataset);
    }
    else if (dataset == 'NLM_WSD_JET') {
        $('#dataset').text('NLM-WSD files from JET experiments');
        $('#inp_dataset').val(dataset);
    }
    else if (dataset != '') {
        $('#dataset').text(dataset);
        $('#inp_dataset').val(dataset);
    }
});
