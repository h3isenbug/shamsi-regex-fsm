class Context:
    def __init__(self):
        self._state = S1(self, '', None)
    
    def handle(self, input):
        self._state.handle(input)

    def is_accept(self):
        return self._state.IS_ACCEPT

    def set_state(self, new_state):
        self._state = new_state

    def back(self):
        return self._state.back()
        
    def get_path(self):
        return self._state.path
        
class BaseState:
    def __init__(self, context, path, previous):
        self._context = context
        self.IS_ACCEPT = False
        self.state_map = {}
        self.path = path
        self.previous = previous
        
    def back(self):
        self._context.set_state(self.previous)
        return not self.previous == None

    def handle(self, input):
        next_state = self.state_map.get(input, DEAD)(self._context, self.path + input, self)
        self._context.set_state(next_state)


class S1(BaseState):
    def __init__(self, context, path, previous):
        BaseState.__init__(self, context, path, previous)
        self.state_map = {
            '0':S2,
            '1':S3,
            '2':S2,
            '3':S2,
            '4':S2,
            '5':S2,
            '6':S2,
            '7':S2,
            '8':S2,
            '9':S2,
        }
        
class S2(BaseState):
    def __init__(self, context, path, previous):
        BaseState.__init__(self, context, path, previous)
        self.state_map = {
            '0':S4,
            '1':S4,
            '2':S4,
            '3':S4,
            '4':S4,
            '5':S4,
            '6':S4,
            '7':S4,
            '8':S4,
            '9':S4,
        }

class S3(BaseState):
    def __init__(self, context, path, previous):
        BaseState.__init__(self, context, path, previous)
        self.state_map = {
            '0':S4,
            '1':S4,
            '2':S4,
            '3':S5,
            '4':S4,
            '5':S4,
            '6':S4,
            '7':S4,
            '8':S4,
            '9':S4,
        }

class S4(BaseState):
    def __init__(self, context, path, previous):
        BaseState.__init__(self, context, path, previous)
        self.state_map = {
            ' ':S6,
            '.':S6,
            '/':S6,
            '-':S6,
        }

class S5(BaseState):
    def __init__(self, context, path, previous):
        BaseState.__init__(self, context, path, previous)
        self.state_map = {
            '0':S2,
            '1':S2,
            '2':S2,
            '3':S2,
            '4':S2,
            '5':S2,
            '6':S2,
            '7':S2,
            '8':S2,
            '9':S2,
            ' ':S6,
            '.':S6,
            '/':S6,
            '-':S6,
        }

class S6(BaseState):
    def __init__(self, context, path, previous):
        BaseState.__init__(self, context, path, previous)
        self.state_map = {
            '0':S7,
            '1':S8,
            '2':S9,
            '3':S9,
            '4':S9,
            '5':S9,
            '6':S9,
            '7':S9,
            '8':S9,
            '9':S9,
        }

class S7(BaseState):
    def __init__(self, context, path, previous):
        BaseState.__init__(self, context, path, previous)
        self.state_map = {
            '1':S8,
            '2':S8,
            '3':S8,
            '4':S8,
            '5':S8,
            '6':S8,
            '7':S8,
            '8':S8,
            '9':S8,
        }

class S8(BaseState):
    def __init__(self, context, path, previous):
        BaseState.__init__(self, context, path, previous)
        self.state_map = {
            '0':S10,
            '1':S10,
            '2':S10,
            ' ':S11,
            '.':S11,
            '/':S11,
            '-':S11,
        }

class S9(BaseState):
    def __init__(self, context, path, previous):
        BaseState.__init__(self, context, path, previous)
        self.state_map = {
            ' ':S11,
            '.':S11,
            '/':S11,
            '-':S11,
        }

class S10(BaseState):
    def __init__(self, context, path, previous):
        BaseState.__init__(self, context, path, previous)
        self.state_map = {
            ' ':S11,
            '.':S11,
            '/':S11,
            '-':S11,
        }

class S11(BaseState):
    def __init__(self, context, path, previous):
        BaseState.__init__(self, context, path, previous)
        self.state_map = {
            '0':S12,
            '1':S13,
            '2':S13,
            '3':S14,
            '4':S15,
            '5':S15,
            '6':S15,
            '7':S15,
            '8':S15,
            '9':S15,
        }

class S12(BaseState):
    def __init__(self, context, path, previous):
        BaseState.__init__(self, context, path, previous)
        self.state_map = {
            '1':S15,
            '2':S15,
            '3':S15,
            '4':S15,
            '5':S15,
            '6':S15,
            '7':S15,
            '8':S15,
            '9':S15,
        }

class S13(BaseState):
    def __init__(self, context, path, previous):
        BaseState.__init__(self, context, path, previous)
        self.IS_ACCEPT = True
        self.state_map = {
            '0':S15,
            '1':S15,
            '2':S15,
            '3':S15,
            '4':S15,
            '5':S15,
            '6':S15,
            '7':S15,
            '8':S15,
            '9':S15,
        }

class S14(BaseState):
    def __init__(self, context, path, previous):
        BaseState.__init__(self, context, path, previous)
        self.IS_ACCEPT = True
        self.state_map = {
            '0':S15,
            '1':S15,
        }

class S15(BaseState):
    def __init__(self, context, path, previous):
        BaseState.__init__(self, context, path, previous)
        self.IS_ACCEPT = True

class DEAD(BaseState):
    def __init__(self, context, path, previous):
        BaseState.__init__(self, context, path, previous)