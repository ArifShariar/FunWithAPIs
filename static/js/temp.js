
        $(document).on('submit','#weather-form', function (e){
            e.preventDefault();
            var district = $('#selectDistrict').val();
            $.ajax({
                url: '/weather/search/',
                type: 'POST',
                data: {
                    district: district,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(data){
                    $('#weather-form').html(data);
                    alert("clicked")
                }
            });
        });
