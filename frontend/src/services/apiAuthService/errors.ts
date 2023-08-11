export class APIError extends Error {
  constructor(message: string) {
    super(message)
    this.name = 'APIError'
  }
}

export class AuthenticationError extends APIError {
  constructor(message: string) {
    super(message)
    this.name = 'AuthenticationError'
  }
}

export class UsernameAlreadyExistsError extends APIError {
  constructor(message: string) {
    super(message)
    this.name = 'UsernameAlreadyExistsError'
  }
}

export class APIResponseMalformedError extends APIError {
  constructor(message: string) {
    super(message)
    this.name = 'APIResponseMalformedError'
  }
}

export class APIServerDownError extends APIError {
  constructor(message: string) {
    super(message)
    this.name = 'APIServerDownError'
  }
}
