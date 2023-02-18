import typewise_constants as tc


def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
  limits = temperature_breach_limit(coolingType)
  return infer_breach(
    temperatureInC,
    limits['lowerLimit'],
    limits['upperLimit']
  )


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  if alertTarget == tc.ALERT_TARGET[0]:
    send_to_controller(
      classify_temperature_breach(
        batteryChar['coolingType'],
        temperatureInC
      )
    )
  elif alertTarget == tc.ALERT_TARGET[1]:
    send_to_email(
      classify_temperature_breach(
        batteryChar['coolingType'],
        temperatureInC
      )
    )
  return classify_temperature_breach(
    batteryChar['coolingType'],
    temperatureInC
  )


def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')


def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}')
    print('Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}')
    print('Hi, the temperature is too high')


def temperature_breach_limit(coolingType):
  return tc.COOLING_TYPE_LIMITS[coolingType]
