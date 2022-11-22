class Calculators:
    @staticmethod
    def durationLinearDecay(initial_value, decay_rate):            
        return initial_value / decay_rate

    @staticmethod
    def durationQuadraticDecay(initial_value, decay_rate):
        return 4*decay_rate*initial_value**0.5/(2*decay_rate)

    @staticmethod
    def durationGeometricSerieDecay(initial_value, decay_rate):
        final_value = initial_value
        duration = 1
        decay_rate = 1.1 if decay_rate == 1 else decay_rate
        while final_value >= 1:
            final_value = initial_value*(decay_rate**(-duration-1))
            duration += 1
        return duration

    @staticmethod
    def durationExponentialDecay(initial_value, decay_rate):
        from numpy import log as ln
        return decay_rate * ln(initial_value)

    @staticmethod
    def linear(initial_value, rise_rate, time):
        return initial_value+rise_rate*time

    @staticmethod
    def quadratic(initial_value, rise_rate, time):
        return initial_value+(rise_rate*time)**2

    @staticmethod
    def exponential(initial_value, rise_rate, time):
        return initial_value+rise_rate**time

class Random:
    @staticmethod
    def limitedProbability(lower_bound=0, upper_bound=100, percentage=True):
        from random import randint
        decimal_adjust = 100
        if upper_bound > 1 and lower_bound < upper_bound:
            value = randint(int(lower_bound*decimal_adjust),int(upper_bound*decimal_adjust))        
        elif upper_bound > 1 and lower_bound > upper_bound:
            value = randint(int(upper_bound*decimal_adjust),int(lower_bound*decimal_adjust))
        elif upper_bound <= 1 and lower_bound <= upper_bound:
            value = randint(int(lower_bound*decimal_adjust**2),int(upper_bound*decimal_adjust**2))        
        elif upper_bound <= 1 and lower_bound > upper_bound:
            value = randint(int(upper_bound*decimal_adjust**2),int(lower_bound*decimal_adjust**2))

        if percentage is True:
            return value/decimal_adjust
        else:
            return value/decimal_adjust/decimal_adjust

class SkillDetrimentalEffects:
    def __init__(self, target_attribute, duration, occurrence_probability, temporal_behavior, effect_area_type) -> None:
        self.target_attribute = target_attribute
        self.duration = duration
        self.occurrence_probability = occurrence_probability
        self.temporal_behavior = temporal_behavior
        self.effect_area_type = effect_area_type

    @staticmethod
    def removePoints(target, effect, removal_rate):
        while effect.duration > 0:
            target.target_attribute -= removal_rate
        return target.target_attribute

    def temporalEffect(countdown):
        import time
        def countdownShow(countdown):
            while countdown:
                print(f'{countdown}')
                time.sleep(1)
                countdown -= 1

class Bleeding(SkillDetrimentalEffects):
    def __init__(self, initial_value, decay_rate, initial_demage, demage_decay_rate, occurrence_probability) -> None:
        self.target_attibute = 'HEALTH POINTS'
        self.effect_area_type = 'TARGET BODY'
        super().__init__(target_attribute=self.target_attibute, occurrence_probability=occurrence_probability, effect_area_type=self.effect_area_type, temporal_behavior = Calculators.durationGeometricSerieDecay(initial_demage, demage_decay_rate), duration = Calculators.durationLinearDecay(initial_value, decay_rate))

class Burn(SkillDetrimentalEffects):
    def __init__(self, duration, occurrence_probability, temporal_behavior) -> None:
        self.target_attribute = 'HEALTH POINTS'
        self.effect_area_type = 'AREA'
        super().__init__(self.target_attribute, duration, occurrence_probability, temporal_behavior, self.effect_area_type)

class Eletrocuted(SkillDetrimentalEffects):
    def __init__(self, duration, occurrence_probability, temporal_behavior) -> None:
        self.target_attribute = 'REACTIONS'
        self.effect_area_type = 'CONTACT'
        super().__init__(self.target_attribute, duration, occurrence_probability, temporal_behavior, self.effect_area_type)

class Freezing(SkillDetrimentalEffects):
    def __init__(self, duration, occurrence_probability, temporal_behavior) -> None:
        self.target_attribute = 'STAMINA POINTS'
        self.effect_area_type = 'AREA'
        super().__init__(self.target_attribute, duration, occurrence_probability, temporal_behavior, self.effect_area_type)

class Blindness(SkillDetrimentalEffects):
    def __init__(self, duration, occurrence_probability, temporal_behavior) -> None:
        self.target_attribute = 'VISION'
        self.effect_area_type = 'TARGET BODY'
        super().__init__(self.target_attribute, duration, occurrence_probability, temporal_behavior, self.effect_area_type)

class Disease(SkillDetrimentalEffects):
    def __init__(self, target_attribute, duration, occurrence_probability, temporal_behavior) -> None:
        self.effect_area_type = 'TARGET BODY'
        super().__init__(target_attribute, duration, occurrence_probability, temporal_behavior, self.effect_area_type)

class AttackSkill:
    def __init__(self, demage_base, critical_rate, critical_demage, ignored_resistence, casting_time, runtime, mana_spend, stamina_spend, health_spend, passive_activation_rate) -> None:
        self.demage_base = demage_base
        self.critical_rate = critical_rate
        self.critical_demage = critical_demage
        self.ignored_resistence = ignored_resistence
        self.casting_time = casting_time
        self.runtime = runtime
        self.mana_spend = mana_spend
        self.stamina_spend = stamina_spend
        self.health_spend = health_spend
        self.passive_activation_rate = passive_activation_rate

    def demage(self):
        p = Random.limitedProbability()
        if p < self.critical_rate:
            demage = self.demage_base*Random.limitedProbability(95,100,False) + self.critical_demage*Random.limitedProbability(percentage=False)
        else:
            demage = self.demage_base*Random.limitedProbability(95,100,False)
        return demage

effect_area_types = ['TARGET BODY', 'USER BODY', 'NEAR USER', 'MISSILE', 'CONTACT', 'JET', 'AREA']
target_attributes = ['HEALTH POINTS', 'MANA POINTS', 'STAMINA POINTS', 'VISION', 'HEARING', 'SMELL', 'REACTIONS', 'SPEED']
