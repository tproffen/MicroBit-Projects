def on_button_pressed_b():
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_button_pressed_a():
    strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
input.on_button_pressed(Button.A, on_button_pressed_a)
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
strip.set_brightness(255)
strip.show_color(neopixel.colors(NeoPixelColors.WHITE))