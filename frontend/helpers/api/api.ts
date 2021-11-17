import axiosModule, { AxiosRequestConfig } from "axios"

export type AccessToken = string

export interface User {
  active: boolean
  role: string
  email: string
  emailConfirmedAt?: string
  firstName?: string
  lastName?: string
  phoneNumber?: string
}

export interface NewUser {
  email: string
  password: string
  firstName?: string
  lastName?: string
  phoneNumber?: string
}

export interface LoginCredentials {
  email: string
  password: string
}

export interface Officer {
  first_name?: string
  last_name?: string
}

export interface UseOfForce {
  item?: string
}
export interface Incident {
  id: number
  location?: string
  time_of_incident?: string
  department?: string
  officers: Officer[]
  description?: string
  use_of_force: UseOfForce[]
  source?: string
}

interface AuthenticatedRequest {
  accessToken: AccessToken
}

export type RegisterRequest = NewUser
export type LoginRequest = LoginCredentials
export type WhoamiRequest = AuthenticatedRequest
export interface IncidentSearchRequest extends AuthenticatedRequest {
  description?: string
  startTime?: string
  endTime?: string
  location?: string
  page?: number
  perPage?: number
}

export type IncidentSearchResponse = {
  results: Incident[]
  page: number
  totalPages: number
  totalResults: number
}

export const baseURL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:5000/api/v1"

const axios = axiosModule.create({
  baseURL,
  timeout: 5000
})

export function login(data: LoginRequest): Promise<AccessToken> {
  return request({
    url: "/auth/login",
    method: "POST",
    data
  }).then(({ access_token }) => access_token)
}

export function register(data: RegisterRequest): Promise<AccessToken> {
  return request({
    url: "/auth/register",
    method: "POST",
    data
  }).then(({ access_token }) => access_token)
}

export function whoami({ accessToken }: WhoamiRequest): Promise<User> {
  return request({
    url: "/auth/test",
    method: "GET",
    accessToken
  }).then(({ active, email, email_confirmed_at, first_name, last_name, phone_number, role }) => ({
    active,
    email,
    emailConfirmedAt: email_confirmed_at,
    firstName: first_name,
    lastName: last_name,
    phoneNumber: phone_number,
    role: role
  }))
}

export function searchIncidents({
  accessToken,
  startTime,
  endTime,
  ...rest
}: IncidentSearchRequest): Promise<IncidentSearchResponse> {
  if (startTime) startTime = new Date(startTime).toISOString()
  if (endTime) endTime = new Date(endTime).toISOString()

  return request({
    url: "/incidents/search",
    method: "POST",
    accessToken,
    data: { startTime, endTime, ...rest }
  })
}

function request({ accessToken, ...config }: AxiosRequestConfig & { accessToken?: AccessToken }) {
  let { headers, ...rest } = config
  if (accessToken) {
    headers = {
      Authorization: `Bearer ${accessToken}`,
      ...headers
    }
  }

  return axios({
    headers,
    ...rest
  }).then((response) => response.data)
}
