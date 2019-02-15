# Format specification for two decimal places:
two_decimal_places = "My body is made of {:.2f}% water".format(77.5548651132)

#Format specification for comma separator:
india_citizen = "The approximate population of {} is {}".format("India",1324000000)

#Format specification for padding and alignment:

left_aligned_padded_20_chars   = "| {:<20} |".format("MY_STRING_VALUE")
center_aligned_padded_20_chars = "| {:^20} |".format("MY_STRING_VALUE")
right_aligned_padded_20_chars  = "| {:>20} |".format("MY_STRING_VALUE")

#Format specification to derive padding width from a variable:
left_aligned  = "| {:<{}} |".format("MY_STRING_VALUE", padding_width)

# Order for format specification:
balance_string = "Your bank balance is {:>20,.2f}"].format(12345.678)