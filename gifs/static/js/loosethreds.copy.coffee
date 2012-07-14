((loosethreds) ->
  loosethreds.copy = ( ->
    self = {}
    inputBase = $('<input type="text" class="input-xlarge image-url">')

    self.init = ->
      base = $('#user_images')

      base.delegate 'button.copy', 'click', (event) ->
        button = $(this)
        input = inputBase.clone()

        input.val(button.data('url'))
        input.attr('data-url', button.data('url'))

        button.replaceWith(input)
        input.focus().select()

      base.delegate 'input.image-url', 'blur', (event) ->
        jnput = $(this)
        button = $('<button class="btn copy">Copy</button>')
        
        button.attr('data-url', input.data('url'))

        input.replaceWith(button.clone())

    return self
  )()
)(loosethreds)

$(document).ready ->
  loosethreds.copy.init()
