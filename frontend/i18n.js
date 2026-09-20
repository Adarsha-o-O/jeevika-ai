const JEEVIKA_LANGUAGES = {
  en: { code: "en", backendName: "English", speech: "en-IN", htmlLang: "en" },
  kn: { code: "kn", backendName: "Kannada", speech: "kn-IN", htmlLang: "kn" },
  hi: { code: "hi", backendName: "Hindi", speech: "hi-IN", htmlLang: "hi" }
};

const translations = {
  en: {
    page_title: "Jeevika AI",
    language_title: "Choose your language",
    language_subtitle: "Jeevika AI will continue in your selected language.",

    continue_english: "Continue in English",
    continue_kannada: "Continue in Kannada",
    continue_hindi: "Continue in Hindi",

    brand_subtitle: "Livelihood Guidance Platform",

    nav_dashboard: "Dashboard",
    nav_profile: "My Profile",
    nav_recommendations: "Recommendations",
    nav_voice: "Jeevika Assistant",
    nav_nsqf: "NSQF & Skills",
    nav_schemes: "Government Schemes",
    nav_opportunities: "Opportunities",

    dashboard_title: "Jeevika AI",
    dashboard_subtitle: "Personalized livelihood and skilling guidance",

    beneficiary_id: "Beneficiary ID",
    load_dashboard: "Load Dashboard",

    beneficiary_profile: "Beneficiary Profile",
    profile_empty: "Load a beneficiary to view the profile.",

    voice_assistant: "Jeevika Assistant",
    speak: "Speak",
    ask_jeevika: "Ask Jeevika",
    waiting_voice: "Waiting for voice input...",
    assistant_placeholder: "Jeevika's response will appear here.",
    assistant_input_placeholder: "Ask about livelihoods, skills, NSQF or schemes...",
    quick_best: "Best livelihood",
    quick_why: "Why this?",
    quick_skills: "Skills to learn",
    quick_nsqf: "NSQF course",
    quick_schemes: "Schemes",
    quick_opportunities: "Opportunities",
    quick_alternatives: "Other options",
    assistant_enter_or_speak: "Type a question or speak first.",
    assistant_thinking: "Jeevika is checking your profile...",
    assistant_quick_question_used: "Quick question selected.",
    assistant_no_profile: "Please create or load your profile first so Jeevika can give personalized guidance.",
    assistant_no_recommendations: "Your profile is saved, but Jeevika does not have a confident livelihood match from the current data. Add specific skills, interests, and work details, then try again.",
    assistant_profile_factors: "your education, interests and work profile",
    assistant_best_response: "Your strongest current match is {occupation} with a {score}% profile match. The main matching factors include {skills}.",
    assistant_why_response: "{occupation} is recommended because your profile matches these factors: {reasons}. Its current profile match is {score}%.",
    assistant_why_profile_response: "{occupation} is ranked from your education, interests, current work and other profile factors. Its current profile match is {score}%.",
    assistant_skills_response: "Across your top livelihood options, the main skills to develop are: {skills}.",
    assistant_no_skill_gaps: "Your current top recommendations do not show a major skill gap in the available data.",
    assistant_nsqf_response: "For {occupation}, the mapped NSQF pathway is {qualification}, Level {level}, Code {code}, with a duration of {duration} hours. Current mapped eligibility: {eligibility}.",
    assistant_nsqf_response_v2: "For {occupation}, {qualification} is mapped as a {pathway}. NSQF Level {level}, Code {code}, duration {duration} hours. Eligibility status: {eligibility}.",
    assistant_no_nsqf: "No verified NSQF qualification is mapped to your current recommendations yet.",
    assistant_eligibility_yes: "Based on the current mapped criteria, you are shown as eligible for {qualification}, linked to {occupation}.",
    assistant_eligibility_no: "Based on the current mapped criteria, you are not yet shown as eligible for {qualification}, linked to {occupation}.",
    assistant_eligibility_verify: "A potentially relevant eligibility route exists for {qualification}, linked to {occupation}, but one or more qualification details still need verification.",
    assistant_nsqf_expired_only: "A historical NSQF record exists for one of your recommendations, but its recorded validity period has ended, so Jeevika is not presenting it as a current pathway.",
    assistant_schemes_response: "Government schemes linked to your top recommendations include: {schemes}. These are guidance matches, not a guarantee of final scheme eligibility.",
    assistant_schemes_response_v2: "The strongest government-scheme matches across your top livelihood options are: {schemes}. These are relevance matches only; official eligibility must still be verified with the scheme authority.",
    assistant_no_schemes: "No government scheme mapping is available for your current recommendations yet.",
    assistant_opportunities_response: "The strongest verified opportunity sources for your top livelihood options are: {sources}. These are official discovery channels, not a guarantee that a live vacancy is currently available.",
    assistant_no_opportunities: "No verified opportunity source is currently matched to your top livelihood recommendations.",
    assistant_alternatives_response: "Other livelihood options from your current profile are: {options}.",
    assistant_no_alternatives: "No additional livelihood alternatives are available in the current recommendation result.",
    assistant_profile_response: "Your profile shows: name {name}; education {education}; current occupation {occupation}; experience {experience} years; skills {skills}.",

    livelihood_recommendations: "Livelihood Recommendations",
    view_details: "View Details",
    hide_details: "Hide Details",
    show_more_recommendations: "Show More Recommendations",
    show_fewer_recommendations: "Show Fewer Recommendations",
    recommendations_empty: "Load a beneficiary to generate recommendations.",

    name: "Name",
    location: "Location",
    education: "Education",
    current_occupation: "Current Occupation",
    experience: "Experience",
    skills: "Skills",
    interests: "Interests",

    years: "years",
    none: "None",
    not_specified: "Not specified",

    matched_skills: "Matched Skills",
    skill_gaps: "Skills to Develop",
    interests_matched: "Matched Interests",

    nsqf_qualification: "NSQF Qualification",
    government_schemes: "Government Schemes",

    scheme_highly_relevant: "Highly relevant",
    scheme_relevant: "Relevant",
    scheme_worth_checking: "Worth checking",
    scheme_benefit: "Potential benefit",
    scheme_why_suggested: "Why Jeevika suggested this",
    scheme_verify_before_applying: "Verify before applying",
    scheme_relevance_not_eligibility: "Jeevika has matched this scheme for relevance. This is not confirmation of official eligibility.",
    scheme_application_mode: "Application mode",
    scheme_information_checked: "Information checked",
    view_official_scheme: "View official scheme",
    scheme_type_skilling: "Skilling / Certification",
    scheme_type_apprenticeship: "Apprenticeship / On-the-job Training",
    scheme_type_self_employment: "Self-employment / Micro-enterprise",
    scheme_type_rural_training: "Rural Skill Training / Placement",
    scheme_type_street_vendor: "Street-vendor Working Capital",
    scheme_type_micro_credit: "Micro-enterprise Credit",

    scheme_reason_skill_gaps: "This livelihood has skill gaps that may benefit from formal training.",
    scheme_reason_nsqf: "Jeevika has an NSQF pathway mapped for this livelihood.",
    scheme_reason_pmkvy_age: "The beneficiary is within the PMKVY Short-Term Training age range.",
    scheme_reason_rpl: "Existing work experience makes Recognition of Prior Learning worth checking.",
    scheme_reason_apprenticeship: "This occupation suits an apprenticeship or on-the-job training pathway.",
    scheme_reason_apprenticeship_age: "The beneficiary meets the general minimum apprenticeship age threshold.",
    scheme_reason_work_based_training: "A mapped skill qualification makes structured work-based training especially relevant.",
    scheme_reason_self_employment: "The livelihood or profile points toward self-employment or a new micro-enterprise.",
    scheme_reason_pmegp_age: "The beneficiary meets the basic PMEGP adult-age condition.",
    scheme_reason_ddu_age: "The beneficiary falls within an age band that can be relevant for DDU-GKY.",
    scheme_reason_rural_signal: "A village/town location is recorded, so rural-programme relevance is worth verifying.",
    scheme_reason_street_vendor: "The occupation/current work explicitly matches a street-vending livelihood.",
    scheme_reason_micro_enterprise: "The livelihood or profile points toward a micro-enterprise/self-employment pathway.",
    scheme_reason_allied_agriculture: "This is an allied-agriculture activity such as poultry, dairy or beekeeping that is within PMMY's stated activity scope.",

    scheme_verify_identity_job_role: "Aadhaar/identity and job-role eligibility",
    scheme_verify_training_availability: "Availability of the relevant approved training pathway",
    scheme_verify_rpl_experience: "Whether prior experience satisfies the selected RPL job role",
    scheme_verify_trade_requirements: "Trade-specific education and physical requirements",
    scheme_verify_apprenticeship_place: "Availability of a registered establishment and apprenticeship contract",
    scheme_verify_new_enterprise: "Whether this is a new eligible enterprise/project",
    scheme_verify_project_rules: "Project activity and project-cost rules",
    scheme_verify_previous_subsidy: "Previous government-subsidy assistance",
    scheme_verify_pmegp_education: "Education requirement where the project-cost threshold makes it applicable",
    scheme_verify_rural_residence: "Rural residence",
    scheme_verify_household_criteria: "Poor-household / programme target-group criteria",
    scheme_verify_ddu_conditions: "Other DDU-GKY admission conditions",
    scheme_verify_vendor_documents: "Street-vendor identification and local-body / scheme documentation requirements",
    scheme_verify_enterprise_details: "Enterprise and loan-purpose details",
    scheme_verify_lender: "Lender appraisal and applicable PMMY category",
    local_opportunities: "Local Opportunities",
    verified_opportunity_sources: "Verified Opportunity Sources",
    opportunity_highly_relevant: "Highly relevant",
    opportunity_relevant: "Relevant",
    opportunity_worth_checking: "Worth checking",
    opportunity_district_source: "District source",
    opportunity_state_source: "State source",
    opportunity_national_source: "National source",
    opportunity_why_useful: "Why this source is useful",
    opportunity_delivery_mode: "Access",
    opportunity_information_checked: "Information checked",
    open_official_portal: "Open official portal",
    opportunity_freshness_default: "Availability can change. Check the official source for current listings.",
    no_verified_opportunity_source: "No verified opportunity source currently matches this livelihood and profile.",

    opportunity_reason_district: "This verified source or listing matches your district.",
    opportunity_reason_state: "This verified source or listing matches your state.",
    opportunity_reason_national: "This verified source is available at national level.",
    opportunity_reason_occupation_match: "The listing directly matches the recommended occupation.",
    opportunity_reason_skillconnect: "You are in Karnataka, and Karnataka SkillConnect is the state's official skills and opportunity platform.",
    opportunity_reason_skillconnect_apprenticeship: "The portal supports apprenticeship and work-based opportunity discovery.",
    opportunity_reason_skillconnect_courses: "The portal also includes courses and employability resources.",
    opportunity_reason_ncs: "National Career Service provides official job-search resources for jobseekers across India.",
    opportunity_reason_ncs_role: "You can use the recommended occupation as the search role/designation on NCS.",
    opportunity_reason_apprenticeship: "This occupation is suitable for an apprenticeship or on-the-job training pathway.",
    opportunity_reason_apprenticeship_nsqf: "A mapped skill qualification makes apprenticeship exploration especially relevant.",
    opportunity_reason_training_gap: "Your recommendation has skill gaps that can be used to search for relevant training.",
    opportunity_reason_training_nsqf: "This livelihood has an NSQF-linked pathway, so verified skill-course discovery is relevant.",

    match: "Match",
    level: "Level",
    code: "Code",
    duration: "Duration",
    hours: "hours",
    eligible: "Eligible",
    yes: "Yes",
    not_yet: "Not yet",

    nsqf_exact_pathway: "Exact pathway",
    nsqf_related_pathway: "Related pathway",
    nsqf_status_eligible: "Eligible",
    nsqf_status_verify: "Needs verification",
    nsqf_status_not_eligible: "Not currently eligible",
    nsqf_validity_active: "Current",
    nsqf_validity_expired: "Expired",
    nsqf_validity_not_active: "Not active yet",
    nsqf_validity_unconfirmed: "Validity unconfirmed",
    valid_until: "Valid until",
    view_official_source: "View official NQR source",
    nsqf_eligibility_routes: "Eligibility routes",
    nsqf_route: "Route",
    minimum_education: "Minimum education",
    experience_required: "Experience required",
    training_requirement: "Training requirement",
    previous_nsqf_level: "Previous NSQF level",
    not_required: "Not required",

    no_recommendations: "No suitable recommendations found.",
    no_skill_match: "No direct skill match",
    no_skill_gap: "No major skill gap",
    no_interest_match: "No direct interest match",
    no_nsqf: "No mapped NSQF qualification available yet",
    nsqf_expired_only: "A historical NSQF record exists for this livelihood, but it is not shown as current guidance because its recorded validity period has ended.",
    no_scheme: "No relevant scheme information available",
    no_opportunity: "No verified local opportunities available yet",

    listening: "Listening...",
    you_said: "You said:",
    voice_error: "Voice error:",
    speak_first: "Please speak first.",
    speech_not_supported: "Speech recognition is not supported in this browser.",

    enter_beneficiary_id: "Enter a beneficiary ID first.",
    beneficiary_not_found: "Beneficiary not found.",
    recommendation_failed: "Could not generate recommendations.",
    assistant_failed: "Jeevika could not process your request.",

    loading: "Loading...",
    change_language: "Language",

    new_profile: "New Profile",
    show_navigation: "Show navigation",
    hide_navigation: "Hide navigation",
    onboarding_manual_mode: "Enter Details",
    onboarding_voice_mode: "Tell Jeevika by Voice",
    voice_onboarding_title: "Voice-guided profile setup",
    voice_onboarding_subtitle: "Jeevika will ask one question at a time. Answer naturally in your selected language.",
    voice_start: "Start Voice Setup",
    voice_retry: "Speak Again",
    voice_confirm_next: "Confirm & Continue",
    voice_skip: "Skip",
    voice_answer_heard: "I heard:",
    voice_waiting_answer: "Press Start Voice Setup when you are ready.",
    voice_question_progress: "Question {current} of {total}",
    voice_listening_now: "Listening for your answer...",
    voice_processing: "Checking your answer...",
    voice_prompting: "Jeevika is asking the question...",
    voice_interview_complete: "Your profile details are ready",
    voice_interview_complete_help: "Review the captured details or create your profile and get recommendations.",
    voice_create_profile: "Create Profile & Find Recommendations",
    voice_edit_manually: "Review / Edit Details",
    voice_unrecognized: "I could not clearly understand that answer. Please speak again.",
    voice_invalid_choice: "I could not match that answer to the available choices. Please speak again.",
    voice_number_not_understood: "I could not understand the number. Please say the number again slowly.",
    voice_microphone_denied: "Microphone access is blocked. Allow microphone access in your browser or use the form.",
    voice_not_supported: "Voice input is not supported in this browser. Please use the form instead.",
    voice_optional_hint: "This question is optional. You can say ‘skip’.",
    voice_review_title: "Captured profile",
    voice_review_note: "These details will be used to create your beneficiary profile.",
    voice_complete_badge: "Ready",
    voice_skip_word: "skip",

    vq_name: "What is your full name?",
    vq_age: "How old are you? Please say your age.",
    vq_gender: "What is your gender? Say male, female, or other.",
    vq_state: "Which state do you live in?",
    vq_district: "Which district do you live in?",
    vq_village: "What is your village or town? You can say skip if you do not want to provide it.",
    vq_education: "What is the highest education you completed? For example, 10th, 12th, ITI, diploma, graduate, or no formal schooling.",
    vq_occupation: "What work do you currently do? Say not working if you are not currently working.",
    vq_experience: "How many years of work experience do you have?",
    vq_skills: "Tell me the skills you already have. You can say more than one skill.",
    vq_interests: "What kind of work are you interested in? You can say more than one interest.",
    vq_income: "What monthly income would you like to earn? You can say zero if you are unsure.",
    vq_relocation: "Are you willing to relocate for work or training? Say yes or no.",
    onboarding_title: "Let's build your profile",
    onboarding_subtitle: "Answer a few simple questions so Jeevika can suggest suitable livelihood pathways.",
    onboarding_step: "Step {current} of {total}",
    step_personal: "Basic Information",
    step_background: "Education & Work",
    step_skills: "Skills & Interests",
    step_goals: "Goals & Preferences",
    full_name: "Full Name",
    age: "Age",
    gender: "Gender",
    select_gender: "Select gender",
    male: "Male",
    female: "Female",
    other: "Other",
    state: "State",
    district: "District",
    village: "Village / Town",
    optional: "Optional",
    education_level: "Highest Education",
    select_education: "Select education level",
    edu_no_school: "No formal schooling",
    edu_primary: "Primary school",
    edu_8th: "8th Standard",
    edu_10th: "10th Standard",
    edu_12th: "12th Standard",
    edu_iti: "ITI",
    edu_diploma: "Diploma",
    edu_graduate: "Graduate",
    edu_postgraduate: "Postgraduate",
    current_occupation_field: "Current Occupation",
    occupation_placeholder: "Example: Two-Wheeler Mechanic",
    experience_years_field: "Years of Experience",
    existing_skills_field: "Existing Skills",
    skills_help: "Enter skills separated by commas.",
    skills_placeholder: "Example: vehicle repair, electrical work, tool handling",
    interests_field: "Work Interests",
    interests_help: "Enter interests separated by commas.",
    interests_placeholder: "Example: automobile servicing, mechanical work",
    income_target_field: "Monthly Income Goal",
    income_target_help: "Enter an approximate amount in rupees. You can leave it as 0 if unsure.",
    relocation_field: "Are you willing to relocate for work or training?",
    relocate_no: "No",
    relocate_yes: "Yes",
    back: "Back",
    continue_button: "Continue",
    create_profile: "Create Profile & Find Recommendations",
    creating_profile: "Creating your profile...",
    profile_create_failed: "Could not create your profile. Please check the details and try again.",
    profile_created: "Profile created successfully. Preparing your recommendations...",
    required_fields: "Please complete all required fields before continuing.",
    skills_required: "Please enter at least one existing skill.",
    interests_required: "Please enter at least one work interest.",
    invalid_age: "Please enter a valid age between 18 and 100.",
    invalid_name: "Enter a real name using letters, not random characters or numbers.",
    invalid_state: "Enter a valid state name.",
    invalid_district: "Enter a valid district name.",
    invalid_village: "Enter a valid village or town name, or leave it blank.",
    invalid_occupation: "Enter a meaningful occupation, or leave it blank if you are not working.",
    invalid_experience: "Enter a valid number of years of experience.",
    experience_age_mismatch: "Experience looks too high for this age. The maximum plausible value here is {max} years.",
    invalid_income: "Enter a monthly income goal between ₹0 and ₹10,00,000.",
    invalid_skill_item: "‘{item}’ does not look like a meaningful skill. Use specific skills such as vehicle repair, welding, tailoring, or tool handling.",
    invalid_interest_item: "‘{item}’ does not look like a meaningful work interest. Use specific interests such as automobile servicing, electrical work, tailoring, or agriculture.",
    too_many_skills: "Please keep the skills list to 12 clear skills or fewer.",
    too_many_interests: "Please keep the interests list to 12 clear interests or fewer.",
    profile_fix_errors: "Please correct the highlighted details before continuing.",
    voice_meaningful_text_needed: "I could not identify a meaningful answer. Please say it again using clear words.",
    no_recommendations_title: "Jeevika needs a little more profile detail",
    no_recommendations_help: "No confident livelihood match was found from the current data. This does not mean there are no suitable livelihoods for you.",
    no_recommendations_tip_skills: "Add specific practical skills instead of very broad or random words.",
    no_recommendations_tip_interests: "Add the kind of work you genuinely want to do.",
    no_recommendations_tip_occupation: "Add your current or previous occupation if you have one.",
    low_confidence_title: "Exploratory matches:",
    low_confidence_help: "The available profile match is relatively weak. Add more specific skills and interests before treating these as strong recommendations.",
    new_profile_confirm: "Start a new profile? The current profile will be cleared from this browser.",
    dashboard_loading: "Preparing your personalized recommendations...",

    recommendation_reason:
      "{occupation} is recommended based on your profile. Matched skills: {skills}. Overall profile match: {score}% as per the current recommendation engine.",

    no_matched_skills_for_reason: "profile factors"
  },

  kn: {
    page_title: "ಜೀವಿಕಾ AI",
    language_title: "ನಿಮ್ಮ ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ",
    language_subtitle: "ನೀವು ಆಯ್ಕೆ ಮಾಡಿದ ಭಾಷೆಯಲ್ಲಿ ಜೀವಿಕಾ AI ಮುಂದುವರಿಯುತ್ತದೆ.",

    continue_english: "ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿ ಮುಂದುವರಿಯಿರಿ",
    continue_kannada: "ಕನ್ನಡದಲ್ಲಿ ಮುಂದುವರಿಯಿರಿ",
    continue_hindi: "ಹಿಂದಿಯಲ್ಲಿ ಮುಂದುವರಿಯಿರಿ",

    brand_subtitle: "ಜೀವನೋಪಾಯ ಮಾರ್ಗದರ್ಶನ ವೇದಿಕೆ",

    nav_dashboard: "ಮುಖಪುಟ",
    nav_profile: "ನನ್ನ ವಿವರಗಳು",
    nav_recommendations: "ಜೀವನೋಪಾಯ ಶಿಫಾರಸುಗಳು",
    nav_voice: "ಜೀವಿಕಾ ಸಹಾಯಕ",
    nav_nsqf: "NSQF ಮತ್ತು ಕೌಶಲ್ಯಗಳು",
    nav_schemes: "ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು",
    nav_opportunities: "ಅವಕಾಶಗಳು",

    dashboard_title: "ಜೀವಿಕಾ AI",
    dashboard_subtitle: "ವೈಯಕ್ತಿಕ ಜೀವನೋಪಾಯ ಮತ್ತು ಕೌಶಲ್ಯ ಮಾರ್ಗದರ್ಶನ",

    beneficiary_id: "ಫಲಾನುಭವಿ ಐಡಿ",
    load_dashboard: "ವಿವರಗಳನ್ನು ತೆರೆಯಿರಿ",

    beneficiary_profile: "ಫಲಾನುಭವಿಯ ವಿವರಗಳು",
    profile_empty: "ಫಲಾನುಭವಿಯ ವಿವರಗಳನ್ನು ನೋಡಲು ಐಡಿ ನಮೂದಿಸಿ.",

    voice_assistant: "ಜೀವಿಕಾ ಸಹಾಯಕ",
    speak: "ಮಾತನಾಡಿ",
    ask_jeevika: "ಜೀವಿಕಾವನ್ನು ಕೇಳಿ",
    waiting_voice: "ಧ್ವನಿ ಮಾಹಿತಿಗಾಗಿ ಕಾಯಲಾಗುತ್ತಿದೆ...",
    assistant_placeholder: "ಜೀವಿಕಾದ ಉತ್ತರ ಇಲ್ಲಿ ಕಾಣಿಸುತ್ತದೆ.",
    assistant_input_placeholder: "ಜೀವನೋಪಾಯ, ಕೌಶಲ್ಯ, NSQF ಅಥವಾ ಯೋಜನೆಗಳ ಬಗ್ಗೆ ಕೇಳಿ...",
    quick_best: "ಉತ್ತಮ ಜೀವನೋಪಾಯ",
    quick_why: "ಏಕೆ ಈ ಆಯ್ಕೆ?",
    quick_skills: "ಕಲಿಯಬೇಕಾದ ಕೌಶಲ್ಯ",
    quick_nsqf: "NSQF ಕೋರ್ಸ್",
    quick_schemes: "ಯೋಜನೆಗಳು",
    quick_opportunities: "ಅವಕಾಶಗಳು",
    quick_alternatives: "ಬೇರೆ ಆಯ್ಕೆಗಳು",
    assistant_enter_or_speak: "ಪ್ರಶ್ನೆಯನ್ನು ಟೈಪ್ ಮಾಡಿ ಅಥವಾ ಮೊದಲು ಮಾತನಾಡಿ.",
    assistant_thinking: "ಜೀವಿಕಾ ನಿಮ್ಮ ಪ್ರೊಫೈಲ್ ಪರಿಶೀಲಿಸುತ್ತಿದೆ...",
    assistant_quick_question_used: "ತ್ವರಿತ ಪ್ರಶ್ನೆ ಆಯ್ಕೆ ಮಾಡಲಾಗಿದೆ.",
    assistant_no_profile: "ವೈಯಕ್ತಿಕ ಮಾರ್ಗದರ್ಶನಕ್ಕಾಗಿ ಮೊದಲು ನಿಮ್ಮ ಪ್ರೊಫೈಲ್ ರಚಿಸಿ ಅಥವಾ ತೆರೆಯಿರಿ.",
    assistant_no_recommendations: "ನಿಮ್ಮ ಪ್ರೊಫೈಲ್ ಉಳಿಸಲಾಗಿದೆ, ಆದರೆ ಪ್ರಸ್ತುತ ಮಾಹಿತಿಯಿಂದ ಜೀವಿಕಾಗೆ ವಿಶ್ವಾಸಾರ್ಹ ಜೀವನೋಪಾಯ ಹೊಂದಾಣಿಕೆ ಸಿಗಲಿಲ್ಲ. ಸ್ಪಷ್ಟವಾದ ಕೌಶಲ್ಯಗಳು, ಆಸಕ್ತಿಗಳು ಮತ್ತು ಕೆಲಸದ ವಿವರಗಳನ್ನು ಸೇರಿಸಿ ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ.",
    assistant_profile_factors: "ನಿಮ್ಮ ಶಿಕ್ಷಣ, ಆಸಕ್ತಿಗಳು ಮತ್ತು ಕೆಲಸದ ಪ್ರೊಫೈಲ್",
    assistant_best_response: "ನಿಮ್ಮ ಪ್ರಸ್ತುತ ಅತ್ಯುತ್ತಮ ಹೊಂದಾಣಿಕೆ {occupation}. ಪ್ರೊಫೈಲ್ ಹೊಂದಾಣಿಕೆ {score}%. ಮುಖ್ಯ ಹೊಂದಾಣಿಕೆಯ ಅಂಶಗಳು: {skills}.",
    assistant_why_response: "{occupation} ಅನ್ನು ಶಿಫಾರಸು ಮಾಡಿರುವುದಕ್ಕೆ ನಿಮ್ಮ ಪ್ರೊಫೈಲ್‌ನ ಈ ಅಂಶಗಳು ಹೊಂದಿಕೆಯಾಗುತ್ತವೆ: {reasons}. ಪ್ರಸ್ತುತ ಹೊಂದಾಣಿಕೆ {score}%.",
    assistant_why_profile_response: "{occupation} ಅನ್ನು ನಿಮ್ಮ ಶಿಕ್ಷಣ, ಆಸಕ್ತಿಗಳು, ಪ್ರಸ್ತುತ ಕೆಲಸ ಮತ್ತು ಇತರ ಪ್ರೊಫೈಲ್ ಅಂಶಗಳ ಆಧಾರದ ಮೇಲೆ ಶ್ರೇಣಿಸಲಾಗಿದೆ. ಪ್ರಸ್ತುತ ಹೊಂದಾಣಿಕೆ {score}%.",
    assistant_skills_response: "ನಿಮ್ಮ ಪ್ರಮುಖ ಜೀವನೋಪಾಯ ಆಯ್ಕೆಗಳಲ್ಲಿ ಅಭಿವೃದ್ಧಿಪಡಿಸಬೇಕಾದ ಮುಖ್ಯ ಕೌಶಲ್ಯಗಳು: {skills}.",
    assistant_no_skill_gaps: "ಲಭ್ಯವಿರುವ ಮಾಹಿತಿಯ ಪ್ರಕಾರ ನಿಮ್ಮ ಪ್ರಮುಖ ಶಿಫಾರಸುಗಳಲ್ಲಿ ದೊಡ್ಡ ಕೌಶಲ್ಯ ಕೊರತೆ ಕಾಣುತ್ತಿಲ್ಲ.",
    assistant_nsqf_response: "{occupation} ಗಾಗಿ ಮ್ಯಾಪ್ ಮಾಡಿರುವ NSQF ಮಾರ್ಗ {qualification}, ಮಟ್ಟ {level}, ಕೋಡ್ {code}, ಅವಧಿ {duration} ಗಂಟೆಗಳು. ಪ್ರಸ್ತುತ ಮ್ಯಾಪ್ ಮಾಡಿದ ಅರ್ಹತೆ: {eligibility}.",
    assistant_nsqf_response_v2: "{occupation} ಗಾಗಿ {qualification} ಅನ್ನು {pathway} ಆಗಿ ಮ್ಯಾಪ್ ಮಾಡಲಾಗಿದೆ. NSQF ಮಟ್ಟ {level}, ಕೋಡ್ {code}, ಅವಧಿ {duration} ಗಂಟೆಗಳು. ಅರ್ಹತಾ ಸ್ಥಿತಿ: {eligibility}.",
    assistant_no_nsqf: "ನಿಮ್ಮ ಪ್ರಸ್ತುತ ಶಿಫಾರಸುಗಳಿಗೆ ಪರಿಶೀಲಿತ NSQF ಅರ್ಹತೆ ಇನ್ನೂ ಮ್ಯಾಪ್ ಮಾಡಲಾಗಿಲ್ಲ.",
    assistant_eligibility_yes: "ಪ್ರಸ್ತುತ ಮ್ಯಾಪ್ ಮಾಡಿದ ಮಾನದಂಡಗಳ ಪ್ರಕಾರ {occupation} ಗೆ ಸಂಬಂಧಿಸಿದ {qualification} ಗೆ ನೀವು ಅರ್ಹರಾಗಿದ್ದೀರಿ ಎಂದು ತೋರಿಸುತ್ತದೆ.",
    assistant_eligibility_no: "ಪ್ರಸ್ತುತ ಮ್ಯಾಪ್ ಮಾಡಿದ ಮಾನದಂಡಗಳ ಪ್ರಕಾರ {occupation} ಗೆ ಸಂಬಂಧಿಸಿದ {qualification} ಗೆ ನೀವು ಇನ್ನೂ ಅರ್ಹರಾಗಿಲ್ಲ ಎಂದು ತೋರಿಸುತ್ತದೆ.",
    assistant_eligibility_verify: "{occupation} ಗೆ ಸಂಬಂಧಿಸಿದ {qualification} ಗಾಗಿ ಒಂದು ಸಾಧ್ಯ ಅರ್ಹತಾ ಮಾರ್ಗ ಇದೆ, ಆದರೆ ಒಂದು ಅಥವಾ ಹೆಚ್ಚಿನ ಅರ್ಹತಾ ವಿವರಗಳನ್ನು ಇನ್ನೂ ಪರಿಶೀಲಿಸಬೇಕಾಗಿದೆ.",
    assistant_nsqf_expired_only: "ನಿಮ್ಮ ಒಂದು ಶಿಫಾರಸಿಗೆ ಹಳೆಯ NSQF ದಾಖಲೆ ಇದೆ, ಆದರೆ ಅದರ ದಾಖಲಾದ ಮಾನ್ಯತಾ ಅವಧಿ ಮುಗಿದಿರುವುದರಿಂದ ಜೀವಿಕಾ ಅದನ್ನು ಪ್ರಸ್ತುತ ಮಾರ್ಗವಾಗಿ ತೋರಿಸುವುದಿಲ್ಲ.",
    assistant_schemes_response: "ನಿಮ್ಮ ಪ್ರಮುಖ ಶಿಫಾರಸುಗಳಿಗೆ ಸಂಬಂಧಿಸಿದ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು: {schemes}. ಇವು ಮಾರ್ಗದರ್ಶನಕ್ಕಾಗಿ ಹೊಂದಿಸಲಾದ ಯೋಜನೆಗಳು; ಅಂತಿಮ ಅರ್ಹತೆಯ ಖಾತರಿ ಅಲ್ಲ.",
    assistant_schemes_response_v2: "ನಿಮ್ಮ ಪ್ರಮುಖ ಜೀವನೋಪಾಯ ಆಯ್ಕೆಗಳಿಗೆ ಹೆಚ್ಚು ಹೊಂದುವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು: {schemes}. ಇವು ಸಂಬಂಧಿತತೆ ಆಧಾರಿತ ಹೊಂದಾಣಿಕೆಗಳು ಮಾತ್ರ; ಅಂತಿಮ ಅಧಿಕೃತ ಅರ್ಹತೆಯನ್ನು ಸಂಬಂಧಿತ ಯೋಜನಾ ಪ್ರಾಧಿಕಾರದಿಂದ ಪರಿಶೀಲಿಸಬೇಕು.",
    assistant_no_schemes: "ನಿಮ್ಮ ಪ್ರಸ್ತುತ ಶಿಫಾರಸುಗಳಿಗೆ ಸರ್ಕಾರಿ ಯೋಜನೆ ಮ್ಯಾಪಿಂಗ್ ಇನ್ನೂ ಲಭ್ಯವಿಲ್ಲ.",
    assistant_opportunities_response: "ನಿಮ್ಮ ಪ್ರಮುಖ ಜೀವನೋಪಾಯ ಆಯ್ಕೆಗಳಿಗೆ ಹೆಚ್ಚು ಹೊಂದುವ ಪರಿಶೀಲಿತ ಅವಕಾಶ ಮೂಲಗಳು: {sources}. ಇವು ಅಧಿಕೃತ ಹುಡುಕಾಟ/ಅವಕಾಶ ಪೋರ್ಟಲ್‌ಗಳು ಮಾತ್ರ; ಪ್ರಸ್ತುತ ಖಾಲಿ ಹುದ್ದೆ ಇದೆ ಎಂಬ ಖಾತರಿ ಅಲ್ಲ.",
    assistant_no_opportunities: "ನಿಮ್ಮ ಪ್ರಮುಖ ಜೀವನೋಪಾಯ ಶಿಫಾರಸುಗಳಿಗೆ ಈಗ ಯಾವುದೇ ಪರಿಶೀಲಿತ ಅವಕಾಶ ಮೂಲ ಹೊಂದಿಕೆಯಾಗಿಲ್ಲ.",
    assistant_alternatives_response: "ನಿಮ್ಮ ಪ್ರಸ್ತುತ ಪ್ರೊಫೈಲ್ ಆಧಾರದ ಮೇಲೆ ಬೇರೆ ಜೀವನೋಪಾಯ ಆಯ್ಕೆಗಳು: {options}.",
    assistant_no_alternatives: "ಪ್ರಸ್ತುತ ಶಿಫಾರಸು ಫಲಿತಾಂಶದಲ್ಲಿ ಹೆಚ್ಚುವರಿ ಜೀವನೋಪಾಯ ಆಯ್ಕೆಗಳು ಲಭ್ಯವಿಲ್ಲ.",
    assistant_profile_response: "ನಿಮ್ಮ ಪ್ರೊಫೈಲ್: ಹೆಸರು {name}; ಶಿಕ್ಷಣ {education}; ಪ್ರಸ್ತುತ ಉದ್ಯೋಗ {occupation}; ಅನುಭವ {experience} ವರ್ಷಗಳು; ಕೌಶಲ್ಯಗಳು {skills}.",

    livelihood_recommendations: "ಜೀವನೋಪಾಯ ಶಿಫಾರಸುಗಳು",
    view_details: "ವಿವರಗಳನ್ನು ನೋಡಿ",
    hide_details: "ವಿವರಗಳನ್ನು ಮರೆಮಾಡಿ",
    show_more_recommendations: "ಇನ್ನಷ್ಟು ಶಿಫಾರಸುಗಳನ್ನು ನೋಡಿ",
    show_fewer_recommendations: "ಕಡಿಮೆ ಶಿಫಾರಸುಗಳನ್ನು ತೋರಿಸಿ",
    recommendations_empty: "ಶಿಫಾರಸುಗಳನ್ನು ಪಡೆಯಲು ಫಲಾನುಭವಿಯನ್ನು ತೆರೆಯಿರಿ.",

    name: "ಹೆಸರು",
    location: "ಸ್ಥಳ",
    education: "ಶಿಕ್ಷಣ",
    current_occupation: "ಪ್ರಸ್ತುತ ಉದ್ಯೋಗ",
    experience: "ಅನುಭವ",
    skills: "ಕೌಶಲ್ಯಗಳು",
    interests: "ಆಸಕ್ತಿಗಳು",

    years: "ವರ್ಷಗಳು",
    none: "ಯಾವುದೂ ಇಲ್ಲ",
    not_specified: "ನೀಡಲಾಗಿಲ್ಲ",

    matched_skills: "ಹೊಂದಿಕೆಯಾಗಿರುವ ಕೌಶಲ್ಯಗಳು",
    skill_gaps: "ಅಭಿವೃದ್ಧಿಪಡಿಸಬೇಕಾದ ಕೌಶಲ್ಯಗಳು",
    interests_matched: "ಹೊಂದಿಕೆಯಾಗಿರುವ ಆಸಕ್ತಿಗಳು",

    nsqf_qualification: "NSQF ಅರ್ಹತೆ",
    government_schemes: "ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು",

    scheme_highly_relevant: "ಹೆಚ್ಚು ಸಂಬಂಧಿತ",
    scheme_relevant: "ಸಂಬಂಧಿತ",
    scheme_worth_checking: "ಪರಿಶೀಲಿಸಲು ಯೋಗ್ಯ",
    scheme_benefit: "ಸಂಭಾವ್ಯ ಪ್ರಯೋಜನ",
    scheme_why_suggested: "ಜೀವಿಕಾ ಇದನ್ನು ಏಕೆ ಸೂಚಿಸಿದೆ",
    scheme_verify_before_applying: "ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮೊದಲು ಪರಿಶೀಲಿಸಿ",
    scheme_relevance_not_eligibility: "ಜೀವಿಕಾ ಈ ಯೋಜನೆಯನ್ನು ಸಂಬಂಧಿತತೆ ಆಧಾರವಾಗಿ ಹೊಂದಿಸಿದೆ. ಇದು ಅಧಿಕೃತ ಅರ್ಹತೆಯ ದೃಢೀಕರಣವಲ್ಲ.",
    scheme_application_mode: "ಅರ್ಜಿ ವಿಧಾನ",
    scheme_information_checked: "ಮಾಹಿತಿ ಪರಿಶೀಲಿಸಿದ ದಿನಾಂಕ",
    view_official_scheme: "ಅಧಿಕೃತ ಯೋಜನೆ ನೋಡಿ",
    scheme_type_skilling: "ಕೌಶಲ್ಯ ತರಬೇತಿ / ಪ್ರಮಾಣೀಕರಣ",
    scheme_type_apprenticeship: "ಅಪ್ರೆಂಟಿಸ್ / ಕೆಲಸದ ಸ್ಥಳದ ತರಬೇತಿ",
    scheme_type_self_employment: "ಸ್ವಯಂ ಉದ್ಯೋಗ / ಸೂಕ್ಷ್ಮ ಉದ್ಯಮ",
    scheme_type_rural_training: "ಗ್ರಾಮೀಣ ಕೌಶಲ್ಯ ತರಬೇತಿ / ಉದ್ಯೋಗ ಸಂಪರ್ಕ",
    scheme_type_street_vendor: "ಬೀದಿ ವ್ಯಾಪಾರಿ ಕಾರ್ಯಾಚರಣೆ ಬಂಡವಾಳ",
    scheme_type_micro_credit: "ಸೂಕ್ಷ್ಮ ಉದ್ಯಮ ಸಾಲ",

    scheme_reason_skill_gaps: "ಈ ಜೀವನೋಪಾಯದಲ್ಲಿ ಅಧಿಕೃತ ತರಬೇತಿಯಿಂದ ಸುಧಾರಿಸಬಹುದಾದ ಕೌಶಲ್ಯ ಅಂತರಗಳಿವೆ.",
    scheme_reason_nsqf: "ಈ ಜೀವನೋಪಾಯಕ್ಕೆ ಜೀವಿಕಾ NSQF ಮಾರ್ಗವನ್ನು ಮ್ಯಾಪ್ ಮಾಡಿದೆ.",
    scheme_reason_pmkvy_age: "ಫಲಾನುಭವಿಯ ವಯಸ್ಸು PMKVY ಅಲ್ಪಾವಧಿ ತರಬೇತಿ ವಯೋಮಿತಿಯೊಳಗೆ ಬರುತ್ತದೆ.",
    scheme_reason_rpl: "ಇರುವ ಕೆಲಸದ ಅನುಭವದಿಂದ Prior Learning Recognition ಮಾರ್ಗವನ್ನು ಪರಿಶೀಲಿಸುವುದು ಉಪಯುಕ್ತವಾಗಬಹುದು.",
    scheme_reason_apprenticeship: "ಈ ಉದ್ಯೋಗವು ಅಪ್ರೆಂಟಿಸ್ ಅಥವಾ ಕೆಲಸದ ಸ್ಥಳದ ತರಬೇತಿಗೆ ಸೂಕ್ತವಾಗಿದೆ.",
    scheme_reason_apprenticeship_age: "ಫಲಾನುಭವಿಯು ಸಾಮಾನ್ಯ ಕನಿಷ್ಠ ಅಪ್ರೆಂಟಿಸ್ ವಯೋಮಿತಿಯನ್ನು ಪೂರೈಸುತ್ತಾರೆ.",
    scheme_reason_work_based_training: "ಮ್ಯಾಪ್ ಮಾಡಿದ ಕೌಶಲ್ಯ ಅರ್ಹತೆ ಇರುವುದರಿಂದ ಸಂರಚಿತ ಕೆಲಸಾಧಾರಿತ ತರಬೇತಿ ಹೆಚ್ಚು ಸಂಬಂಧಿತವಾಗಿದೆ.",
    scheme_reason_self_employment: "ಈ ಜೀವನೋಪಾಯ ಅಥವಾ ಪ್ರೊಫೈಲ್ ಸ್ವಯಂ ಉದ್ಯೋಗ ಅಥವಾ ಹೊಸ ಸೂಕ್ಷ್ಮ ಉದ್ಯಮದ ದಾರಿಗೆ ಸೂಚಿಸುತ್ತದೆ.",
    scheme_reason_pmegp_age: "ಫಲಾನುಭವಿಯು PMEGP ಯ ಮೂಲ ವಯೋಮಿತಿಯನ್ನು ಪೂರೈಸುತ್ತಾರೆ.",
    scheme_reason_ddu_age: "ಫಲಾನುಭವಿಯ ವಯಸ್ಸು DDU-GKY ಗೆ ಸಂಬಂಧಿಸಬಹುದಾದ ವಯೋಮಿತಿಯೊಳಗೆ ಬರುತ್ತದೆ.",
    scheme_reason_rural_signal: "ಗ್ರಾಮ/ಪಟ್ಟಣ ಸ್ಥಳ ಮಾಹಿತಿ ಇರುವುದರಿಂದ ಗ್ರಾಮೀಣ ಯೋಜನೆ ಸಂಬಂಧಿತತೆಯನ್ನು ಪರಿಶೀಲಿಸುವುದು ಯೋಗ್ಯ.",
    scheme_reason_street_vendor: "ಪ್ರಸ್ತುತ ಉದ್ಯೋಗವು ಸ್ಪಷ್ಟವಾಗಿ ಬೀದಿ ವ್ಯಾಪಾರ ಜೀವನೋಪಾಯಕ್ಕೆ ಹೊಂದಿದೆ.",
    scheme_reason_micro_enterprise: "ಜೀವನೋಪಾಯ ಅಥವಾ ಪ್ರೊಫೈಲ್ ಸೂಕ್ಷ್ಮ ಉದ್ಯಮ / ಸ್ವಯಂ ಉದ್ಯೋಗದ ದಾರಿಗೆ ಸೂಚಿಸುತ್ತದೆ.",
    scheme_reason_allied_agriculture: "ಇದು ಕೋಳಿ ಸಾಕಣೆ, ಹೈನುಗಾರಿಕೆ ಅಥವಾ ಜೇನು ಸಾಕಣೆ ಮುಂತಾದ PMMY ವ್ಯಾಪ್ತಿಯ ಕೃಷಿ-ಸಹಾಯಕ ಚಟುವಟಿಕೆಯಾಗಿದೆ.",

    scheme_verify_identity_job_role: "ಆಧಾರ್/ಗುರುತು ಮತ್ತು ಆಯ್ದ ಕೆಲಸದ ಪಾತ್ರದ ಅರ್ಹತೆ",
    scheme_verify_training_availability: "ಸಂಬಂಧಿತ ಅನುಮೋದಿತ ತರಬೇತಿ ಮಾರ್ಗದ ಲಭ್ಯತೆ",
    scheme_verify_rpl_experience: "ಹಿಂದಿನ ಅನುಭವವು ಆಯ್ದ RPL ಕೆಲಸದ ಪಾತ್ರಕ್ಕೆ ಸಾಕಾಗುತ್ತದೆಯೇ",
    scheme_verify_trade_requirements: "ವೃತ್ತಿ-ನಿರ್ದಿಷ್ಟ ಶಿಕ್ಷಣ ಮತ್ತು ದೈಹಿಕ ಅವಶ್ಯಕತೆಗಳು",
    scheme_verify_apprenticeship_place: "ನೋಂದಾಯಿತ ಸಂಸ್ಥೆ ಮತ್ತು ಅಪ್ರೆಂಟಿಸ್ ಒಪ್ಪಂದದ ಲಭ್ಯತೆ",
    scheme_verify_new_enterprise: "ಇದು ಹೊಸ ಅರ್ಹ ಉದ್ಯಮ/ಯೋಜನೆಯೇ",
    scheme_verify_project_rules: "ಯೋಜನಾ ಚಟುವಟಿಕೆ ಮತ್ತು ಯೋಜನಾ ವೆಚ್ಚ ನಿಯಮಗಳು",
    scheme_verify_previous_subsidy: "ಹಿಂದಿನ ಸರ್ಕಾರಿ ಸಬ್ಸಿಡಿ ಸಹಾಯ",
    scheme_verify_pmegp_education: "ಯೋಜನಾ ವೆಚ್ಚ ಮಿತಿಯ ಪ್ರಕಾರ ಅನ್ವಯಿಸುವ ಶಿಕ್ಷಣ ಅವಶ್ಯಕತೆ",
    scheme_verify_rural_residence: "ಗ್ರಾಮೀಣ ವಾಸಸ್ಥಳ",
    scheme_verify_household_criteria: "ಬಡ ಕುಟುಂಬ / ಯೋಜನೆಯ ಗುರಿ ಗುಂಪಿನ ಮಾನದಂಡಗಳು",
    scheme_verify_ddu_conditions: "ಇತರೆ DDU-GKY ಪ್ರವೇಶ ಷರತ್ತುಗಳು",
    scheme_verify_vendor_documents: "ಬೀದಿ ವ್ಯಾಪಾರಿ ಗುರುತು ಮತ್ತು ಸ್ಥಳೀಯ ಸಂಸ್ಥೆ / ಯೋಜನಾ ದಾಖಲೆಗಳು",
    scheme_verify_enterprise_details: "ಉದ್ಯಮ ಮತ್ತು ಸಾಲದ ಉದ್ದೇಶದ ವಿವರಗಳು",
    scheme_verify_lender: "ಸಾಲದಾತರ ಮೌಲ್ಯಮಾಪನ ಮತ್ತು ಅನ್ವಯಿಸುವ PMMY ವರ್ಗ",
    local_opportunities: "ಸ್ಥಳೀಯ ಅವಕಾಶಗಳು",
    verified_opportunity_sources: "ಪರಿಶೀಲಿತ ಅವಕಾಶ ಮೂಲಗಳು",
    opportunity_highly_relevant: "ಹೆಚ್ಚು ಸಂಬಂಧಿತ",
    opportunity_relevant: "ಸಂಬಂಧಿತ",
    opportunity_worth_checking: "ಪರಿಶೀಲಿಸಲು ಯೋಗ್ಯ",
    opportunity_district_source: "ಜಿಲ್ಲಾ ಮಟ್ಟದ ಮೂಲ",
    opportunity_state_source: "ರಾಜ್ಯ ಮಟ್ಟದ ಮೂಲ",
    opportunity_national_source: "ರಾಷ್ಟ್ರೀಯ ಮೂಲ",
    opportunity_why_useful: "ಈ ಮೂಲ ಏಕೆ ಉಪಯುಕ್ತ",
    opportunity_delivery_mode: "ಪ್ರವೇಶ ವಿಧಾನ",
    opportunity_information_checked: "ಮಾಹಿತಿ ಪರಿಶೀಲಿಸಿದ ದಿನಾಂಕ",
    open_official_portal: "ಅಧಿಕೃತ ಪೋರ್ಟಲ್ ತೆರೆಯಿರಿ",
    opportunity_freshness_default: "ಲಭ್ಯತೆ ಬದಲಾಗಬಹುದು. ಪ್ರಸ್ತುತ ಅವಕಾಶಗಳಿಗಾಗಿ ಅಧಿಕೃತ ಮೂಲವನ್ನು ಪರಿಶೀಲಿಸಿ.",
    no_verified_opportunity_source: "ಈ ಜೀವನೋಪಾಯ ಮತ್ತು ಪ್ರೊಫೈಲ್‌ಗೆ ಈಗ ಯಾವುದೇ ಪರಿಶೀಲಿತ ಅವಕಾಶ ಮೂಲ ಹೊಂದಿಕೆಯಾಗಿಲ್ಲ.",

    opportunity_reason_district: "ಈ ಪರಿಶೀಲಿತ ಮೂಲ ಅಥವಾ ಪಟ್ಟಿಯು ನಿಮ್ಮ ಜಿಲ್ಲೆಗೆ ಹೊಂದಿದೆ.",
    opportunity_reason_state: "ಈ ಪರಿಶೀಲಿತ ಮೂಲ ಅಥವಾ ಪಟ್ಟಿಯು ನಿಮ್ಮ ರಾಜ್ಯಕ್ಕೆ ಹೊಂದಿದೆ.",
    opportunity_reason_national: "ಈ ಪರಿಶೀಲಿತ ಮೂಲ ರಾಷ್ಟ್ರೀಯ ಮಟ್ಟದಲ್ಲಿ ಲಭ್ಯವಿದೆ.",
    opportunity_reason_occupation_match: "ಈ ಪಟ್ಟಿ ಶಿಫಾರಸು ಮಾಡಿದ ಉದ್ಯೋಗಕ್ಕೆ ನೇರವಾಗಿ ಹೊಂದಿದೆ.",
    opportunity_reason_skillconnect: "ನೀವು ಕರ್ನಾಟಕದಲ್ಲಿರುವುದರಿಂದ ಕರ್ನಾಟಕ SkillConnect ರಾಜ್ಯದ ಅಧಿಕೃತ ಕೌಶಲ್ಯ ಮತ್ತು ಅವಕಾಶ ಪೋರ್ಟಲ್ ಆಗಿದೆ.",
    opportunity_reason_skillconnect_apprenticeship: "ಈ ಪೋರ್ಟಲ್ ಅಪ್ರೆಂಟಿಸ್ ಮತ್ತು ಕೆಲಸಾಧಾರಿತ ಅವಕಾಶಗಳ ಹುಡುಕಾಟವನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ.",
    opportunity_reason_skillconnect_courses: "ಈ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಕೋರ್ಸ್‌ಗಳು ಮತ್ತು ಉದ್ಯೋಗಾರ್ಹತೆ ಸಂಪನ್ಮೂಲಗಳೂ ಇವೆ.",
    opportunity_reason_ncs: "National Career Service ಭಾರತದೆಲ್ಲೆಡೆ ಉದ್ಯೋಗ ಹುಡುಕುವವರಿಗೆ ಅಧಿಕೃತ ಉದ್ಯೋಗ ಹುಡುಕಾಟ ಸಂಪನ್ಮೂಲಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ.",
    opportunity_reason_ncs_role: "ಶಿಫಾರಸು ಮಾಡಿದ ಉದ್ಯೋಗವನ್ನು NCS ನಲ್ಲಿ ಹುಡುಕಾಟದ ಕೆಲಸದ ಹೆಸರಾಗಿ ಬಳಸಬಹುದು.",
    opportunity_reason_apprenticeship: "ಈ ಉದ್ಯೋಗವು ಅಪ್ರೆಂಟಿಸ್ ಅಥವಾ ಕೆಲಸದ ಸ್ಥಳದ ತರಬೇತಿಗೆ ಸೂಕ್ತವಾಗಿದೆ.",
    opportunity_reason_apprenticeship_nsqf: "ಮ್ಯಾಪ್ ಮಾಡಿದ ಕೌಶಲ್ಯ ಅರ್ಹತೆ ಇರುವುದರಿಂದ ಅಪ್ರೆಂಟಿಸ್ ಅವಕಾಶಗಳ ಹುಡುಕಾಟ ಹೆಚ್ಚು ಸಂಬಂಧಿತವಾಗಿದೆ.",
    opportunity_reason_training_gap: "ನಿಮ್ಮ ಶಿಫಾರಸಿನಲ್ಲಿ ಕಂಡುಬಂದ ಕೌಶಲ್ಯ ಅಂತರಗಳನ್ನು ಸಂಬಂಧಿತ ತರಬೇತಿ ಹುಡುಕಲು ಬಳಸಬಹುದು.",
    opportunity_reason_training_nsqf: "ಈ ಜೀವನೋಪಾಯಕ್ಕೆ NSQF ಸಂಬಂಧಿತ ಮಾರ್ಗ ಇರುವುದರಿಂದ ಪರಿಶೀಲಿತ ಕೌಶಲ್ಯ ಕೋರ್ಸ್ ಹುಡುಕಾಟ ಸಂಬಂಧಿತವಾಗಿದೆ.",

    match: "ಹೊಂದಾಣಿಕೆ",
    level: "ಮಟ್ಟ",
    code: "ಕೋಡ್",
    duration: "ಅವಧಿ",
    hours: "ಗಂಟೆಗಳು",
    eligible: "ಅರ್ಹತೆ",
    yes: "ಹೌದು",
    not_yet: "ಇನ್ನೂ ಇಲ್ಲ",

    nsqf_exact_pathway: "ನೇರ ಹೊಂದಾಣಿಕೆಯ ಮಾರ್ಗ",
    nsqf_related_pathway: "ಸಂಬಂಧಿತ ಕೌಶಲ್ಯ ಮಾರ್ಗ",
    nsqf_status_eligible: "ಅರ್ಹ",
    nsqf_status_verify: "ಹೆಚ್ಚುವರಿ ಪರಿಶೀಲನೆ ಅಗತ್ಯ",
    nsqf_status_not_eligible: "ಪ್ರಸ್ತುತ ಅರ್ಹತೆ ಇಲ್ಲ",
    nsqf_validity_active: "ಪ್ರಸ್ತುತ ಮಾನ್ಯ",
    nsqf_validity_expired: "ಮಾನ್ಯತೆ ಮುಗಿದಿದೆ",
    nsqf_validity_not_active: "ಇನ್ನೂ ಸಕ್ರಿಯವಾಗಿಲ್ಲ",
    nsqf_validity_unconfirmed: "ಮಾನ್ಯತಾ ಅವಧಿ ದೃಢಪಡಿಸಿಲ್ಲ",
    valid_until: "ಮಾನ್ಯತೆ ಇರುವ ದಿನಾಂಕ",
    view_official_source: "ಅಧಿಕೃತ NQR ಮೂಲ ನೋಡಿ",
    nsqf_eligibility_routes: "ಅರ್ಹತಾ ಮಾರ್ಗಗಳು",
    nsqf_route: "ಮಾರ್ಗ",
    minimum_education: "ಕನಿಷ್ಠ ಶಿಕ್ಷಣ",
    experience_required: "ಅಗತ್ಯ ಅನುಭವ",
    training_requirement: "ತರಬೇತಿ ಅರ್ಹತೆ",
    previous_nsqf_level: "ಹಿಂದಿನ NSQF ಮಟ್ಟ",
    not_required: "ಅಗತ್ಯವಿಲ್ಲ",

    no_recommendations: "ಸೂಕ್ತ ಜೀವನೋಪಾಯ ಶಿಫಾರಸುಗಳು ಲಭ್ಯವಿಲ್ಲ.",
    no_skill_match: "ನೇರ ಕೌಶಲ್ಯ ಹೊಂದಾಣಿಕೆ ಇಲ್ಲ",
    no_skill_gap: "ಪ್ರಮುಖ ಕೌಶಲ್ಯ ಕೊರತೆ ಇಲ್ಲ",
    no_interest_match: "ನೇರ ಆಸಕ್ತಿ ಹೊಂದಾಣಿಕೆ ಇಲ್ಲ",
    no_nsqf: "ಸಂಬಂಧಿತ NSQF ಅರ್ಹತೆ ಇನ್ನೂ ಲಭ್ಯವಿಲ್ಲ",
    nsqf_expired_only: "ಈ ಜೀವನೋಪಾಯಕ್ಕೆ ಹಳೆಯ NSQF ದಾಖಲೆ ಇದೆ, ಆದರೆ ಅದರ ದಾಖಲಾದ ಮಾನ್ಯತಾ ಅವಧಿ ಮುಗಿದಿರುವುದರಿಂದ ಅದನ್ನು ಪ್ರಸ್ತುತ ಮಾರ್ಗದರ್ಶನವಾಗಿ ತೋರಿಸಲಾಗುವುದಿಲ್ಲ.",
    no_scheme: "ಸಂಬಂಧಿತ ಯೋಜನೆ ಮಾಹಿತಿ ಲಭ್ಯವಿಲ್ಲ",
    no_opportunity: "ಪರಿಶೀಲಿತ ಸ್ಥಳೀಯ ಅವಕಾಶಗಳು ಇನ್ನೂ ಲಭ್ಯವಿಲ್ಲ",

    listening: "ಕೇಳಲಾಗುತ್ತಿದೆ...",
    you_said: "ನೀವು ಹೇಳಿದ್ದು:",
    voice_error: "ಧ್ವನಿ ದೋಷ:",
    speak_first: "ಮೊದಲು ಮಾತನಾಡಿ.",
    speech_not_supported: "ಈ ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಧ್ವನಿ ಗುರುತಿಸುವಿಕೆ ಲಭ್ಯವಿಲ್ಲ.",

    enter_beneficiary_id: "ಮೊದಲು ಫಲಾನುಭವಿ ಐಡಿ ನಮೂದಿಸಿ.",
    beneficiary_not_found: "ಫಲಾನುಭವಿ ಕಂಡುಬಂದಿಲ್ಲ.",
    recommendation_failed: "ಜೀವನೋಪಾಯ ಶಿಫಾರಸುಗಳನ್ನು ಸೃಷ್ಟಿಸಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ.",
    assistant_failed: "ನಿಮ್ಮ ವಿನಂತಿಯನ್ನು ಜೀವಿಕಾ ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ.",

    loading: "ಲೋಡ್ ಆಗುತ್ತಿದೆ...",
    change_language: "ಭಾಷೆ",

    new_profile: "ಹೊಸ ಪ್ರೊಫೈಲ್",
    show_navigation: "ನ್ಯಾವಿಗೇಶನ್ ತೋರಿಸಿ",
    hide_navigation: "ನ್ಯಾವಿಗೇಶನ್ ಮರೆಮಾಡಿ",
    onboarding_manual_mode: "ವಿವರಗಳನ್ನು ನಮೂದಿಸಿ",
    onboarding_voice_mode: "ಧ್ವನಿ ಮೂಲಕ ಜೀವಿಕಾಗೆ ಹೇಳಿ",
    voice_onboarding_title: "ಧ್ವನಿ ಮಾರ್ಗದರ್ಶನದ ಪ್ರೊಫೈಲ್",
    voice_onboarding_subtitle: "ಜೀವಿಕಾ ಒಂದೊಂದು ಪ್ರಶ್ನೆ ಕೇಳುತ್ತದೆ. ನೀವು ಆಯ್ಕೆ ಮಾಡಿದ ಭಾಷೆಯಲ್ಲಿ ಸಹಜವಾಗಿ ಉತ್ತರಿಸಿ.",
    voice_start: "ಧ್ವನಿ ಮಾರ್ಗದರ್ಶನ ಪ್ರಾರಂಭಿಸಿ",
    voice_retry: "ಮತ್ತೆ ಹೇಳಿ",
    voice_confirm_next: "ಸರಿಯಾಗಿದೆ, ಮುಂದುವರಿಸಿ",
    voice_skip: "ಬಿಡಿ",
    voice_answer_heard: "ನಾನು ಕೇಳಿದ್ದು:",
    voice_waiting_answer: "ಸಿದ್ಧರಾದಾಗ ‘ಧ್ವನಿ ಮಾರ್ಗದರ್ಶನ ಪ್ರಾರಂಭಿಸಿ’ ಒತ್ತಿರಿ.",
    voice_question_progress: "ಪ್ರಶ್ನೆ {current} / {total}",
    voice_listening_now: "ನಿಮ್ಮ ಉತ್ತರವನ್ನು ಕೇಳಲಾಗುತ್ತಿದೆ...",
    voice_processing: "ನಿಮ್ಮ ಉತ್ತರವನ್ನು ಪರಿಶೀಲಿಸಲಾಗುತ್ತಿದೆ...",
    voice_prompting: "ಜೀವಿಕಾ ಪ್ರಶ್ನೆಯನ್ನು ಕೇಳುತ್ತಿದೆ...",
    voice_interview_complete: "ನಿಮ್ಮ ಪ್ರೊಫೈಲ್ ವಿವರಗಳು ಸಿದ್ಧವಾಗಿವೆ",
    voice_interview_complete_help: "ಸಂಗ್ರಹಿಸಿದ ವಿವರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ ಅಥವಾ ಪ್ರೊಫೈಲ್ ರಚಿಸಿ ಶಿಫಾರಸುಗಳನ್ನು ಪಡೆಯಿರಿ.",
    voice_create_profile: "ಪ್ರೊಫೈಲ್ ರಚಿಸಿ ಮತ್ತು ಶಿಫಾರಸುಗಳನ್ನು ನೋಡಿ",
    voice_edit_manually: "ವಿವರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ / ತಿದ್ದುಪಡಿ ಮಾಡಿ",
    voice_unrecognized: "ನಿಮ್ಮ ಉತ್ತರ ಸ್ಪಷ್ಟವಾಗಿ ಅರ್ಥವಾಗಲಿಲ್ಲ. ದಯವಿಟ್ಟು ಮತ್ತೆ ಹೇಳಿ.",
    voice_invalid_choice: "ನಿಮ್ಮ ಉತ್ತರವನ್ನು ಲಭ್ಯವಿರುವ ಆಯ್ಕೆಗಳಿಗೆ ಹೊಂದಿಸಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ. ದಯವಿಟ್ಟು ಮತ್ತೆ ಹೇಳಿ.",
    voice_number_not_understood: "ಸಂಖ್ಯೆಯನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲಾಗಲಿಲ್ಲ. ದಯವಿಟ್ಟು ಸಂಖ್ಯೆಯನ್ನು ನಿಧಾನವಾಗಿ ಮತ್ತೆ ಹೇಳಿ.",
    voice_microphone_denied: "ಮೈಕ್ರೋಫೋನ್ ಅನುಮತಿ ನಿರ್ಬಂಧಿಸಲಾಗಿದೆ. ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಮೈಕ್ರೋಫೋನ್ ಅನುಮತಿಸಿ ಅಥವಾ ಫಾರ್ಮ್ ಬಳಸಿ.",
    voice_not_supported: "ಈ ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಧ್ವನಿ ಇನ್‌ಪುಟ್ ಲಭ್ಯವಿಲ್ಲ. ದಯವಿಟ್ಟು ಫಾರ್ಮ್ ಬಳಸಿ.",
    voice_optional_hint: "ಈ ಪ್ರಶ್ನೆ ಐಚ್ಛಿಕ. ನೀವು ‘ಬಿಡಿ’ ಎಂದು ಹೇಳಬಹುದು.",
    voice_review_title: "ಸಂಗ್ರಹಿಸಿದ ಪ್ರೊಫೈಲ್",
    voice_review_note: "ಈ ವಿವರಗಳನ್ನು ನಿಮ್ಮ ಫಲಾನುಭವಿ ಪ್ರೊಫೈಲ್ ರಚಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ.",
    voice_complete_badge: "ಸಿದ್ಧ",
    voice_skip_word: "ಬಿಡಿ",

    vq_name: "ನಿಮ್ಮ ಪೂರ್ಣ ಹೆಸರು ಏನು?",
    vq_age: "ನಿಮ್ಮ ವಯಸ್ಸು ಎಷ್ಟು? ವಯಸ್ಸನ್ನು ಸಂಖ್ಯೆಯಾಗಿ ಹೇಳಿ.",
    vq_gender: "ನಿಮ್ಮ ಲಿಂಗ ಯಾವುದು? ಪುರುಷ, ಮಹಿಳೆ ಅಥವಾ ಇತರೆ ಎಂದು ಹೇಳಿ.",
    vq_state: "ನೀವು ಯಾವ ರಾಜ್ಯದಲ್ಲಿ ವಾಸಿಸುತ್ತೀರಿ?",
    vq_district: "ನೀವು ಯಾವ ಜಿಲ್ಲೆಯಲ್ಲಿ ವಾಸಿಸುತ್ತೀರಿ?",
    vq_village: "ನಿಮ್ಮ ಊರು ಅಥವಾ ಪಟ್ಟಣದ ಹೆಸರು ಏನು? ನೀಡಲು ಇಷ್ಟವಿಲ್ಲದಿದ್ದರೆ ‘ಬಿಡಿ’ ಎಂದು ಹೇಳಿ.",
    vq_education: "ನೀವು ಪೂರ್ಣಗೊಳಿಸಿದ ಅತ್ಯುನ್ನತ ಶಿಕ್ಷಣ ಯಾವುದು? ಉದಾಹರಣೆಗೆ 10ನೇ, 12ನೇ, ಐಟಿಐ, ಡಿಪ್ಲೊಮಾ, ಪದವಿ ಅಥವಾ ಔಪಚಾರಿಕ ಶಿಕ್ಷಣ ಇಲ್ಲ ಎಂದು ಹೇಳಿ.",
    vq_occupation: "ನೀವು ಈಗ ಯಾವ ಕೆಲಸ ಮಾಡುತ್ತೀರಿ? ಕೆಲಸ ಮಾಡುತ್ತಿಲ್ಲದಿದ್ದರೆ ‘ಕೆಲಸ ಇಲ್ಲ’ ಎಂದು ಹೇಳಿ.",
    vq_experience: "ನಿಮಗೆ ಎಷ್ಟು ವರ್ಷಗಳ ಕೆಲಸದ ಅನುಭವ ಇದೆ?",
    vq_skills: "ನಿಮಗೆ ಈಗಿರುವ ಕೌಶಲ್ಯಗಳನ್ನು ಹೇಳಿ. ಒಂದಕ್ಕಿಂತ ಹೆಚ್ಚು ಕೌಶಲ್ಯಗಳನ್ನು ಹೇಳಬಹುದು.",
    vq_interests: "ನಿಮಗೆ ಯಾವ ರೀತಿಯ ಕೆಲಸದಲ್ಲಿ ಆಸಕ್ತಿ ಇದೆ? ಒಂದಕ್ಕಿಂತ ಹೆಚ್ಚು ಆಸಕ್ತಿಗಳನ್ನು ಹೇಳಬಹುದು.",
    vq_income: "ತಿಂಗಳಿಗೆ ಎಷ್ಟು ಆದಾಯ ಪಡೆಯಲು ಬಯಸುತ್ತೀರಿ? ಖಚಿತವಾಗಿಲ್ಲದಿದ್ದರೆ ಸೊನ್ನೆ ಎಂದು ಹೇಳಬಹುದು.",
    vq_relocation: "ಕೆಲಸ ಅಥವಾ ತರಬೇತಿಗಾಗಿ ಬೇರೆ ಸ್ಥಳಕ್ಕೆ ಹೋಗಲು ಸಿದ್ಧರಿದ್ದೀರಾ? ಹೌದು ಅಥವಾ ಇಲ್ಲ ಎಂದು ಹೇಳಿ.",
    onboarding_title: "ನಿಮ್ಮ ಪ್ರೊಫೈಲ್ ನಿರ್ಮಿಸೋಣ",
    onboarding_subtitle: "ನಿಮಗೆ ಸೂಕ್ತವಾದ ಜೀವನೋಪಾಯ ಮಾರ್ಗಗಳನ್ನು ಸೂಚಿಸಲು ಕೆಲವು ಸರಳ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸಿ.",
    onboarding_step: "ಹಂತ {current} / {total}",
    step_personal: "ಮೂಲ ಮಾಹಿತಿ",
    step_background: "ಶಿಕ್ಷಣ ಮತ್ತು ಕೆಲಸ",
    step_skills: "ಕೌಶಲ್ಯಗಳು ಮತ್ತು ಆಸಕ್ತಿಗಳು",
    step_goals: "ಗುರಿಗಳು ಮತ್ತು ಆದ್ಯತೆಗಳು",
    full_name: "ಪೂರ್ಣ ಹೆಸರು",
    age: "ವಯಸ್ಸು",
    gender: "ಲಿಂಗ",
    select_gender: "ಲಿಂಗವನ್ನು ಆಯ್ಕೆಮಾಡಿ",
    male: "ಪುರುಷ",
    female: "ಮಹಿಳೆ",
    other: "ಇತರೆ",
    state: "ರಾಜ್ಯ",
    district: "ಜಿಲ್ಲೆ",
    village: "ಗ್ರಾಮ / ಪಟ್ಟಣ",
    optional: "ಐಚ್ಛಿಕ",
    education_level: "ಗರಿಷ್ಠ ಶಿಕ್ಷಣ",
    select_education: "ಶಿಕ್ಷಣ ಮಟ್ಟವನ್ನು ಆಯ್ಕೆಮಾಡಿ",
    edu_no_school: "ಔಪಚಾರಿಕ ಶಿಕ್ಷಣ ಇಲ್ಲ",
    edu_primary: "ಪ್ರಾಥಮಿಕ ಶಾಲೆ",
    edu_8th: "8ನೇ ತರಗತಿ",
    edu_10th: "10ನೇ ತರಗತಿ",
    edu_12th: "12ನೇ ತರಗತಿ",
    edu_iti: "ಐಟಿಐ",
    edu_diploma: "ಡಿಪ್ಲೊಮಾ",
    edu_graduate: "ಪದವಿ",
    edu_postgraduate: "ಸ್ನಾತಕೋತ್ತರ",
    current_occupation_field: "ಪ್ರಸ್ತುತ ಉದ್ಯೋಗ",
    occupation_placeholder: "ಉದಾಹರಣೆ: ದ್ವಿಚಕ್ರ ವಾಹನ ಮೆಕ್ಯಾನಿಕ್",
    experience_years_field: "ಕೆಲಸದ ಅನುಭವ (ವರ್ಷಗಳು)",
    existing_skills_field: "ಈಗಿರುವ ಕೌಶಲ್ಯಗಳು",
    skills_help: "ಕೌಶಲ್ಯಗಳನ್ನು ಅಲ್ಪವಿರಾಮದಿಂದ ಬೇರ್ಪಡಿಸಿ ಬರೆಯಿರಿ.",
    skills_placeholder: "ಉದಾಹರಣೆ: ವಾಹನ ದುರಸ್ತಿ, ವಿದ್ಯುತ್ ಕೆಲಸ, ಉಪಕರಣ ಬಳಕೆ",
    interests_field: "ಕೆಲಸದ ಆಸಕ್ತಿಗಳು",
    interests_help: "ಆಸಕ್ತಿಗಳನ್ನು ಅಲ್ಪವಿರಾಮದಿಂದ ಬೇರ್ಪಡಿಸಿ ಬರೆಯಿರಿ.",
    interests_placeholder: "ಉದಾಹರಣೆ: ವಾಹನ ಸರ್ವಿಸಿಂಗ್, ಯಾಂತ್ರಿಕ ಕೆಲಸ",
    income_target_field: "ತಿಂಗಳ ಆದಾಯ ಗುರಿ",
    income_target_help: "ಅಂದಾಜು ಮೊತ್ತವನ್ನು ರೂಪಾಯಿಗಳಲ್ಲಿ ನಮೂದಿಸಿ. ಖಚಿತವಿಲ್ಲದಿದ್ದರೆ 0 ಇರಿಸಬಹುದು.",
    relocation_field: "ಕೆಲಸ ಅಥವಾ ತರಬೇತಿಗಾಗಿ ಸ್ಥಳಾಂತರಗೊಳ್ಳಲು ಸಿದ್ಧರಿದ್ದೀರಾ?",
    relocate_no: "ಇಲ್ಲ",
    relocate_yes: "ಹೌದು",
    back: "ಹಿಂದೆ",
    continue_button: "ಮುಂದುವರಿಸಿ",
    create_profile: "ಪ್ರೊಫೈಲ್ ರಚಿಸಿ ಮತ್ತು ಶಿಫಾರಸುಗಳನ್ನು ನೋಡಿ",
    creating_profile: "ನಿಮ್ಮ ಪ್ರೊಫೈಲ್ ರಚಿಸಲಾಗುತ್ತಿದೆ...",
    profile_create_failed: "ಪ್ರೊಫೈಲ್ ರಚಿಸಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ. ವಿವರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ.",
    profile_created: "ಪ್ರೊಫೈಲ್ ಯಶಸ್ವಿಯಾಗಿ ರಚಿಸಲಾಗಿದೆ. ಶಿಫಾರಸುಗಳನ್ನು ಸಿದ್ಧಪಡಿಸಲಾಗುತ್ತಿದೆ...",
    required_fields: "ಮುಂದುವರಿಯುವ ಮೊದಲು ಅಗತ್ಯ ಮಾಹಿತಿಯನ್ನು ಪೂರ್ಣಗೊಳಿಸಿ.",
    skills_required: "ಕನಿಷ್ಠ ಒಂದು ಕೌಶಲ್ಯವನ್ನು ನಮೂದಿಸಿ.",
    interests_required: "ಕನಿಷ್ಠ ಒಂದು ಕೆಲಸದ ಆಸಕ್ತಿಯನ್ನು ನಮೂದಿಸಿ.",
    invalid_age: "18 ರಿಂದ 100ರ ನಡುವೆ ಸರಿಯಾದ ವಯಸ್ಸನ್ನು ನಮೂದಿಸಿ.",
    invalid_name: "ಅಕ್ಷರಗಳನ್ನು ಬಳಸಿ ಸರಿಯಾದ ಹೆಸರನ್ನು ನಮೂದಿಸಿ; ಯಾದೃಚ್ಛಿಕ ಅಕ್ಷರಗಳು ಅಥವಾ ಸಂಖ್ಯೆಗಳು ಬೇಡ.",
    invalid_state: "ಸರಿಯಾದ ರಾಜ್ಯದ ಹೆಸರನ್ನು ನಮೂದಿಸಿ.",
    invalid_district: "ಸರಿಯಾದ ಜಿಲ್ಲೆಯ ಹೆಸರನ್ನು ನಮೂದಿಸಿ.",
    invalid_village: "ಸರಿಯಾದ ಗ್ರಾಮ ಅಥವಾ ಪಟ್ಟಣದ ಹೆಸರನ್ನು ನಮೂದಿಸಿ, ಅಥವಾ ಖಾಲಿ ಬಿಡಿ.",
    invalid_occupation: "ಅರ್ಥಪೂರ್ಣ ಉದ್ಯೋಗವನ್ನು ನಮೂದಿಸಿ, ಅಥವಾ ಈಗ ಕೆಲಸ ಮಾಡದಿದ್ದರೆ ಖಾಲಿ ಬಿಡಿ.",
    invalid_experience: "ಅನುಭವದ ವರ್ಷಗಳಿಗೆ ಸರಿಯಾದ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ.",
    experience_age_mismatch: "ಈ ವಯಸ್ಸಿಗೆ ಅನುಭವದ ವರ್ಷಗಳು ಹೆಚ್ಚು ಕಾಣುತ್ತಿವೆ. ಇಲ್ಲಿ ಗರಿಷ್ಠ ಸಮಂಜಸ ಮೌಲ್ಯ {max} ವರ್ಷಗಳು.",
    invalid_income: "ಮಾಸಿಕ ಆದಾಯ ಗುರಿಯನ್ನು ₹0 ರಿಂದ ₹10,00,000ರ ನಡುವೆ ನಮೂದಿಸಿ.",
    invalid_skill_item: "‘{item}’ ಅರ್ಥಪೂರ್ಣ ಕೌಶಲ್ಯವಾಗಿ ಕಾಣುತ್ತಿಲ್ಲ. ವಾಹನ ದುರಸ್ತಿ, ವೆಲ್ಡಿಂಗ್, ಹೊಲಿಗೆ ಅಥವಾ ಉಪಕರಣ ಬಳಕೆ ಮುಂತಾದ ಸ್ಪಷ್ಟ ಕೌಶಲ್ಯಗಳನ್ನು ನಮೂದಿಸಿ.",
    invalid_interest_item: "‘{item}’ ಅರ್ಥಪೂರ್ಣ ಕೆಲಸದ ಆಸಕ್ತಿಯಾಗಿ ಕಾಣುತ್ತಿಲ್ಲ. ವಾಹನ ಸರ್ವಿಸಿಂಗ್, ವಿದ್ಯುತ್ ಕೆಲಸ, ಹೊಲಿಗೆ ಅಥವಾ ಕೃಷಿ ಮುಂತಾದ ಸ್ಪಷ್ಟ ಆಸಕ್ತಿಗಳನ್ನು ನಮೂದಿಸಿ.",
    too_many_skills: "ಕೌಶಲ್ಯಗಳ ಪಟ್ಟಿಯನ್ನು 12 ಸ್ಪಷ್ಟ ಕೌಶಲ್ಯಗಳಿಗೆ ಅಥವಾ ಅದಕ್ಕಿಂತ ಕಡಿಮೆಗೆ ಮಿತಿಗೊಳಿಸಿ.",
    too_many_interests: "ಆಸಕ್ತಿಗಳ ಪಟ್ಟಿಯನ್ನು 12 ಸ್ಪಷ್ಟ ಆಸಕ್ತಿಗಳಿಗೆ ಅಥವಾ ಅದಕ್ಕಿಂತ ಕಡಿಮೆಗೆ ಮಿತಿಗೊಳಿಸಿ.",
    profile_fix_errors: "ಮುಂದುವರಿಯುವ ಮೊದಲು ಗುರುತಿಸಲಾದ ವಿವರಗಳನ್ನು ಸರಿಪಡಿಸಿ.",
    voice_meaningful_text_needed: "ಅರ್ಥಪೂರ್ಣ ಉತ್ತರವನ್ನು ಗುರುತಿಸಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ. ದಯವಿಟ್ಟು ಸ್ಪಷ್ಟವಾಗಿ ಮತ್ತೆ ಹೇಳಿ.",
    no_recommendations_title: "ಜೀವಿಕಾಗೆ ಇನ್ನಷ್ಟು ಪ್ರೊಫೈಲ್ ವಿವರಗಳು ಬೇಕಾಗಿವೆ",
    no_recommendations_help: "ಪ್ರಸ್ತುತ ಮಾಹಿತಿಯಿಂದ ವಿಶ್ವಾಸಾರ್ಹ ಜೀವನೋಪಾಯ ಹೊಂದಾಣಿಕೆ ಸಿಗಲಿಲ್ಲ. ಇದರರ್ಥ ನಿಮಗೆ ಸೂಕ್ತ ಜೀವನೋಪಾಯವೇ ಇಲ್ಲ ಎಂಬುದಲ್ಲ.",
    no_recommendations_tip_skills: "ಬಹಳ ಸಾಮಾನ್ಯ ಅಥವಾ ಯಾದೃಚ್ಛಿಕ ಪದಗಳ ಬದಲು ಸ್ಪಷ್ಟ ಪ್ರಾಯೋಗಿಕ ಕೌಶಲ್ಯಗಳನ್ನು ಸೇರಿಸಿ.",
    no_recommendations_tip_interests: "ನೀವು ನಿಜವಾಗಿಯೂ ಮಾಡಲು ಬಯಸುವ ಕೆಲಸದ ರೀತಿಯನ್ನು ಸೇರಿಸಿ.",
    no_recommendations_tip_occupation: "ಇದ್ದರೆ ನಿಮ್ಮ ಪ್ರಸ್ತುತ ಅಥವಾ ಹಿಂದಿನ ಉದ್ಯೋಗವನ್ನು ಸೇರಿಸಿ.",
    low_confidence_title: "ಪರಿಶೀಲನಾ ಮಟ್ಟದ ಹೊಂದಾಣಿಕೆಗಳು:",
    low_confidence_help: "ಲಭ್ಯವಿರುವ ಪ್ರೊಫೈಲ್ ಹೊಂದಾಣಿಕೆ ತುಸು ದುರ್ಬಲವಾಗಿದೆ. ಇವುಗಳನ್ನು ಬಲವಾದ ಶಿಫಾರಸುಗಳೆಂದು ಪರಿಗಣಿಸುವ ಮೊದಲು ಇನ್ನಷ್ಟು ಸ್ಪಷ್ಟ ಕೌಶಲ್ಯಗಳು ಮತ್ತು ಆಸಕ್ತಿಗಳನ್ನು ಸೇರಿಸಿ.",
    new_profile_confirm: "ಹೊಸ ಪ್ರೊಫೈಲ್ ಆರಂಭಿಸಬೇಕೇ? ಈ ಬ್ರೌಸರ್‌ನಲ್ಲಿರುವ ಪ್ರಸ್ತುತ ಪ್ರೊಫೈಲ್ ತೆರವುಗೊಳ್ಳುತ್ತದೆ.",
    dashboard_loading: "ನಿಮ್ಮ ವೈಯಕ್ತಿಕ ಶಿಫಾರಸುಗಳನ್ನು ಸಿದ್ಧಪಡಿಸಲಾಗುತ್ತಿದೆ...",

    recommendation_reason:
      "{occupation} ನಿಮ್ಮ ವಿವರಗಳ ಆಧಾರದ ಮೇಲೆ ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ. ಹೊಂದಿಕೆಯಾಗಿರುವ ಕೌಶಲ್ಯಗಳು: {skills}. ಪ್ರಸ್ತುತ ಶಿಫಾರಸು ವ್ಯವಸ್ಥೆಯ ಪ್ರಕಾರ ಒಟ್ಟು ಹೊಂದಾಣಿಕೆ: {score}%.",

    no_matched_skills_for_reason: "ಪ್ರೊಫೈಲ್ ಅಂಶಗಳು"
  },

  hi: {
    page_title: "जीविका AI",
    language_title: "अपनी भाषा चुनें",
    language_subtitle: "जीविका AI आपकी चुनी हुई भाषा में आगे चलेगा।",

    continue_english: "अंग्रेज़ी में जारी रखें",
    continue_kannada: "कन्नड़ में जारी रखें",
    continue_hindi: "हिन्दी में जारी रखें",

    brand_subtitle: "आजीविका मार्गदर्शन मंच",

    nav_dashboard: "मुखपृष्ठ",
    nav_profile: "मेरी जानकारी",
    nav_recommendations: "आजीविका सुझाव",
    nav_voice: "जीविका सहायक",
    nav_nsqf: "NSQF और कौशल",
    nav_schemes: "सरकारी योजनाएँ",
    nav_opportunities: "अवसर",

    dashboard_title: "जीविका AI",
    dashboard_subtitle: "व्यक्तिगत आजीविका और कौशल मार्गदर्शन",

    beneficiary_id: "लाभार्थी आईडी",
    load_dashboard: "जानकारी खोलें",

    beneficiary_profile: "लाभार्थी की जानकारी",
    profile_empty: "लाभार्थी की जानकारी देखने के लिए आईडी दर्ज करें।",

    voice_assistant: "जीविका सहायक",
    speak: "बोलें",
    ask_jeevika: "जीविका से पूछें",
    waiting_voice: "आवाज़ की प्रतीक्षा की जा रही है...",
    assistant_placeholder: "जीविका का उत्तर यहाँ दिखाई देगा।",
    assistant_input_placeholder: "आजीविका, कौशल, NSQF या योजनाओं के बारे में पूछें...",
    quick_best: "सबसे उपयुक्त आजीविका",
    quick_why: "यह क्यों?",
    quick_skills: "कौन से कौशल सीखें",
    quick_nsqf: "NSQF कोर्स",
    quick_schemes: "योजनाएँ",
    quick_opportunities: "अवसर",
    quick_alternatives: "अन्य विकल्प",
    assistant_enter_or_speak: "प्रश्न टाइप करें या पहले बोलें।",
    assistant_thinking: "जीविका आपकी प्रोफ़ाइल देख रहा है...",
    assistant_quick_question_used: "त्वरित प्रश्न चुना गया।",
    assistant_no_profile: "व्यक्तिगत मार्गदर्शन के लिए पहले अपनी प्रोफ़ाइल बनाएँ या खोलें।",
    assistant_no_recommendations: "आपकी प्रोफ़ाइल सुरक्षित है, लेकिन वर्तमान जानकारी से जीविका को भरोसेमंद आजीविका मिलान नहीं मिला। स्पष्ट कौशल, रुचियाँ और काम का विवरण जोड़कर फिर प्रयास करें।",
    assistant_profile_factors: "आपकी शिक्षा, रुचियाँ और कार्य प्रोफ़ाइल",
    assistant_best_response: "आपकी वर्तमान सबसे मजबूत आजीविका मिलान {occupation} है, जिसका प्रोफ़ाइल मेल {score}% है। मुख्य मिलान कारक हैं: {skills}.",
    assistant_why_response: "{occupation} इसलिए सुझाया गया है क्योंकि आपकी प्रोफ़ाइल के ये कारक मेल खाते हैं: {reasons}. वर्तमान प्रोफ़ाइल मेल {score}% है।",
    assistant_why_profile_response: "{occupation} को आपकी शिक्षा, रुचियों, वर्तमान कार्य और अन्य प्रोफ़ाइल कारकों के आधार पर रैंक किया गया है। वर्तमान प्रोफ़ाइल मेल {score}% है।",
    assistant_skills_response: "आपके प्रमुख आजीविका विकल्पों में विकसित किए जाने वाले मुख्य कौशल हैं: {skills}.",
    assistant_no_skill_gaps: "उपलब्ध जानकारी में आपकी वर्तमान प्रमुख सिफारिशों में कोई बड़ी कौशल कमी नहीं दिखती।",
    assistant_nsqf_response: "{occupation} के लिए मैप किया गया NSQF मार्ग {qualification}, स्तर {level}, कोड {code}, अवधि {duration} घंटे है। वर्तमान मैप की गई पात्रता: {eligibility}.",
    assistant_nsqf_response_v2: "{occupation} के लिए {qualification} को {pathway} के रूप में मैप किया गया है। NSQF स्तर {level}, कोड {code}, अवधि {duration} घंटे। पात्रता स्थिति: {eligibility}.",
    assistant_no_nsqf: "आपकी वर्तमान सिफारिशों के लिए अभी कोई सत्यापित NSQF योग्यता मैप नहीं है।",
    assistant_eligibility_yes: "वर्तमान मैप किए गए मानदंडों के अनुसार आप {occupation} से जुड़ी {qualification} के लिए पात्र दिखाए गए हैं।",
    assistant_eligibility_no: "वर्तमान मैप किए गए मानदंडों के अनुसार आप {occupation} से जुड़ी {qualification} के लिए अभी पात्र नहीं दिखाए गए हैं।",
    assistant_eligibility_verify: "{occupation} से जुड़ी {qualification} के लिए एक संभावित पात्रता मार्ग है, लेकिन एक या अधिक योग्यता विवरणों की अभी पुष्टि आवश्यक है।",
    assistant_nsqf_expired_only: "आपकी एक सिफारिश के लिए पुराना NSQF रिकॉर्ड मौजूद है, लेकिन उसकी दर्ज वैधता अवधि समाप्त हो चुकी है, इसलिए जीविका उसे वर्तमान मार्ग के रूप में नहीं दिखा रहा है।",
    assistant_schemes_response: "आपकी प्रमुख सिफारिशों से जुड़ी सरकारी योजनाएँ हैं: {schemes}. ये मार्गदर्शन के लिए मिलान हैं, अंतिम योजना पात्रता की गारंटी नहीं।",
    assistant_schemes_response_v2: "आपके प्रमुख आजीविका विकल्पों से सबसे मजबूत सरकारी-योजना मिलान हैं: {schemes}. ये केवल प्रासंगिकता आधारित मिलान हैं; अंतिम आधिकारिक पात्रता संबंधित योजना प्राधिकरण से सत्यापित करनी होगी.",
    assistant_no_schemes: "आपकी वर्तमान सिफारिशों के लिए अभी सरकारी योजना मैपिंग उपलब्ध नहीं है।",
    assistant_opportunities_response: "आपके प्रमुख आजीविका विकल्पों के लिए सबसे मजबूत सत्यापित अवसर स्रोत हैं: {sources}. ये आधिकारिक अवसर/खोज पोर्टल हैं; यह किसी लाइव रिक्ति की गारंटी नहीं है.",
    assistant_no_opportunities: "आपकी प्रमुख आजीविका सिफारिशों से अभी कोई सत्यापित अवसर स्रोत मेल नहीं खाता.",
    assistant_alternatives_response: "आपकी वर्तमान प्रोफ़ाइल के अन्य आजीविका विकल्प हैं: {options}.",
    assistant_no_alternatives: "वर्तमान सिफारिश परिणाम में अतिरिक्त आजीविका विकल्प उपलब्ध नहीं हैं।",
    assistant_profile_response: "आपकी प्रोफ़ाइल: नाम {name}; शिक्षा {education}; वर्तमान व्यवसाय {occupation}; अनुभव {experience} वर्ष; कौशल {skills}.",

    livelihood_recommendations: "आजीविका सुझाव",
    view_details: "विवरण देखें",
    hide_details: "विवरण छिपाएँ",
    show_more_recommendations: "और सुझाव देखें",
    show_fewer_recommendations: "कम सुझाव दिखाएँ",
    recommendations_empty: "सुझाव पाने के लिए लाभार्थी की जानकारी खोलें।",

    name: "नाम",
    location: "स्थान",
    education: "शिक्षा",
    current_occupation: "वर्तमान व्यवसाय",
    experience: "अनुभव",
    skills: "कौशल",
    interests: "रुचियाँ",

    years: "वर्ष",
    none: "कोई नहीं",
    not_specified: "उल्लेख नहीं किया गया",

    matched_skills: "मिलते हुए कौशल",
    skill_gaps: "विकसित किए जाने वाले कौशल",
    interests_matched: "मिलती हुई रुचियाँ",

    nsqf_qualification: "NSQF योग्यता",
    government_schemes: "सरकारी योजनाएँ",

    scheme_highly_relevant: "बहुत प्रासंगिक",
    scheme_relevant: "प्रासंगिक",
    scheme_worth_checking: "जाँचने योग्य",
    scheme_benefit: "संभावित लाभ",
    scheme_why_suggested: "जीविका ने इसे क्यों सुझाया",
    scheme_verify_before_applying: "आवेदन से पहले सत्यापित करें",
    scheme_relevance_not_eligibility: "जीविका ने इस योजना को प्रासंगिकता के आधार पर मिलाया है। यह आधिकारिक पात्रता की पुष्टि नहीं है.",
    scheme_application_mode: "आवेदन का तरीका",
    scheme_information_checked: "जानकारी जाँची गई",
    view_official_scheme: "आधिकारिक योजना देखें",
    scheme_type_skilling: "कौशल प्रशिक्षण / प्रमाणन",
    scheme_type_apprenticeship: "अप्रेंटिसशिप / कार्यस्थल प्रशिक्षण",
    scheme_type_self_employment: "स्वरोज़गार / सूक्ष्म उद्यम",
    scheme_type_rural_training: "ग्रामीण कौशल प्रशिक्षण / प्लेसमेंट",
    scheme_type_street_vendor: "स्ट्रीट-वेंडर कार्यशील पूंजी",
    scheme_type_micro_credit: "सूक्ष्म उद्यम ऋण",

    scheme_reason_skill_gaps: "इस आजीविका में ऐसे कौशल अंतर हैं जिन्हें औपचारिक प्रशिक्षण से सुधारा जा सकता है.",
    scheme_reason_nsqf: "जीविका ने इस आजीविका के लिए एक NSQF मार्ग मैप किया है.",
    scheme_reason_pmkvy_age: "लाभार्थी की आयु PMKVY अल्पकालीन प्रशिक्षण की आयु सीमा में आती है.",
    scheme_reason_rpl: "मौजूदा कार्य-अनुभव के कारण Recognition of Prior Learning मार्ग की जाँच उपयोगी हो सकती है.",
    scheme_reason_apprenticeship: "यह व्यवसाय अप्रेंटिसशिप या कार्यस्थल प्रशिक्षण के लिए उपयुक्त है.",
    scheme_reason_apprenticeship_age: "लाभार्थी सामान्य न्यूनतम अप्रेंटिस आयु सीमा पूरी करते हैं.",
    scheme_reason_work_based_training: "मैप की गई कौशल योग्यता के कारण संरचित कार्य-आधारित प्रशिक्षण विशेष रूप से प्रासंगिक है.",
    scheme_reason_self_employment: "यह आजीविका या प्रोफ़ाइल स्वरोज़गार या नए सूक्ष्म उद्यम की दिशा दिखाती है.",
    scheme_reason_pmegp_age: "लाभार्थी PMEGP की मूल वयस्क-आयु शर्त पूरी करते हैं.",
    scheme_reason_ddu_age: "लाभार्थी की आयु DDU-GKY के लिए प्रासंगिक हो सकने वाली सीमा में आती है.",
    scheme_reason_rural_signal: "गाँव/कस्बे का स्थान दर्ज है, इसलिए ग्रामीण कार्यक्रम की प्रासंगिकता सत्यापित करना उचित है.",
    scheme_reason_street_vendor: "वर्तमान काम स्पष्ट रूप से स्ट्रीट-वेंडिंग आजीविका से मेल खाता है.",
    scheme_reason_micro_enterprise: "आजीविका या प्रोफ़ाइल सूक्ष्म उद्यम / स्वरोज़गार की दिशा दिखाती है.",
    scheme_reason_allied_agriculture: "यह पोल्ट्री, डेयरी या मधुमक्खी पालन जैसी कृषि-सहायक गतिविधि है जो PMMY के बताए दायरे में आती है.",

    scheme_verify_identity_job_role: "आधार/पहचान और जॉब-रोल पात्रता",
    scheme_verify_training_availability: "संबंधित स्वीकृत प्रशिक्षण मार्ग की उपलब्धता",
    scheme_verify_rpl_experience: "क्या पिछला अनुभव चुने गए RPL जॉब रोल के लिए पर्याप्त है",
    scheme_verify_trade_requirements: "ट्रेड-विशिष्ट शिक्षा और शारीरिक आवश्यकताएँ",
    scheme_verify_apprenticeship_place: "पंजीकृत प्रतिष्ठान और अप्रेंटिसशिप अनुबंध की उपलब्धता",
    scheme_verify_new_enterprise: "क्या यह नया पात्र उद्यम/परियोजना है",
    scheme_verify_project_rules: "परियोजना गतिविधि और परियोजना-लागत नियम",
    scheme_verify_previous_subsidy: "पिछली सरकारी सब्सिडी सहायता",
    scheme_verify_pmegp_education: "जहाँ परियोजना-लागत सीमा लागू हो वहाँ शिक्षा की शर्त",
    scheme_verify_rural_residence: "ग्रामीण निवास",
    scheme_verify_household_criteria: "गरीब परिवार / कार्यक्रम लक्ष्य-समूह मानदंड",
    scheme_verify_ddu_conditions: "अन्य DDU-GKY प्रवेश शर्तें",
    scheme_verify_vendor_documents: "स्ट्रीट-वेंडर पहचान और स्थानीय निकाय / योजना दस्तावेज़",
    scheme_verify_enterprise_details: "उद्यम और ऋण-उद्देश्य का विवरण",
    scheme_verify_lender: "ऋणदाता मूल्यांकन और लागू PMMY श्रेणी",
    local_opportunities: "स्थानीय अवसर",
    verified_opportunity_sources: "सत्यापित अवसर स्रोत",
    opportunity_highly_relevant: "बहुत प्रासंगिक",
    opportunity_relevant: "प्रासंगिक",
    opportunity_worth_checking: "जाँचने योग्य",
    opportunity_district_source: "जिला स्रोत",
    opportunity_state_source: "राज्य स्रोत",
    opportunity_national_source: "राष्ट्रीय स्रोत",
    opportunity_why_useful: "यह स्रोत क्यों उपयोगी है",
    opportunity_delivery_mode: "पहुंच",
    opportunity_information_checked: "जानकारी जाँची गई",
    open_official_portal: "आधिकारिक पोर्टल खोलें",
    opportunity_freshness_default: "उपलब्धता बदल सकती है। वर्तमान अवसरों के लिए आधिकारिक स्रोत देखें.",
    no_verified_opportunity_source: "इस आजीविका और प्रोफ़ाइल के लिए अभी कोई सत्यापित अवसर स्रोत मेल नहीं खाता.",

    opportunity_reason_district: "यह सत्यापित स्रोत या सूची आपके जिले से मेल खाती है.",
    opportunity_reason_state: "यह सत्यापित स्रोत या सूची आपके राज्य से मेल खाती है.",
    opportunity_reason_national: "यह सत्यापित स्रोत राष्ट्रीय स्तर पर उपलब्ध है.",
    opportunity_reason_occupation_match: "यह सूची सुझाए गए व्यवसाय से सीधे मेल खाती है.",
    opportunity_reason_skillconnect: "आप कर्नाटक में हैं और Karnataka SkillConnect राज्य का आधिकारिक कौशल और अवसर प्लेटफ़ॉर्म है.",
    opportunity_reason_skillconnect_apprenticeship: "यह पोर्टल अप्रेंटिसशिप और कार्य-आधारित अवसर खोजने में भी मदद करता है.",
    opportunity_reason_skillconnect_courses: "इस पोर्टल में कोर्स और रोजगार-योग्यता संसाधन भी शामिल हैं.",
    opportunity_reason_ncs: "National Career Service पूरे भारत में नौकरी चाहने वालों के लिए आधिकारिक नौकरी-खोज संसाधन प्रदान करता है.",
    opportunity_reason_ncs_role: "आप सुझाए गए व्यवसाय को NCS पर खोज भूमिका/पदनाम के रूप में इस्तेमाल कर सकते हैं.",
    opportunity_reason_apprenticeship: "यह व्यवसाय अप्रेंटिसशिप या कार्यस्थल प्रशिक्षण के लिए उपयुक्त है.",
    opportunity_reason_apprenticeship_nsqf: "मैप की गई कौशल योग्यता के कारण अप्रेंटिसशिप अवसर खोजना विशेष रूप से प्रासंगिक है.",
    opportunity_reason_training_gap: "आपकी सिफारिश में पहचाने गए कौशल अंतर का उपयोग संबंधित प्रशिक्षण खोजने के लिए किया जा सकता है.",
    opportunity_reason_training_nsqf: "इस आजीविका का NSQF-संबंधित मार्ग है, इसलिए सत्यापित कौशल-कोर्स खोजना प्रासंगिक है.",

    match: "मेल",
    level: "स्तर",
    code: "कोड",
    duration: "अवधि",
    hours: "घंटे",
    eligible: "पात्र",
    yes: "हाँ",
    not_yet: "अभी नहीं",

    nsqf_exact_pathway: "सीधा मार्ग",
    nsqf_related_pathway: "संबंधित कौशल मार्ग",
    nsqf_status_eligible: "पात्र",
    nsqf_status_verify: "अतिरिक्त पुष्टि आवश्यक",
    nsqf_status_not_eligible: "वर्तमान में पात्र नहीं",
    nsqf_validity_active: "वर्तमान",
    nsqf_validity_expired: "समाप्त",
    nsqf_validity_not_active: "अभी सक्रिय नहीं",
    nsqf_validity_unconfirmed: "वैधता की पुष्टि नहीं",
    valid_until: "इस तारीख तक वैध",
    view_official_source: "आधिकारिक NQR स्रोत देखें",
    nsqf_eligibility_routes: "पात्रता मार्ग",
    nsqf_route: "मार्ग",
    minimum_education: "न्यूनतम शिक्षा",
    experience_required: "आवश्यक अनुभव",
    training_requirement: "प्रशिक्षण आवश्यकता",
    previous_nsqf_level: "पिछला NSQF स्तर",
    not_required: "आवश्यक नहीं",

    no_recommendations: "उपयुक्त आजीविका सुझाव उपलब्ध नहीं हैं।",
    no_skill_match: "सीधा कौशल मेल नहीं मिला",
    no_skill_gap: "कोई प्रमुख कौशल कमी नहीं",
    no_interest_match: "सीधी रुचि का मेल नहीं मिला",
    no_nsqf: "संबंधित NSQF योग्यता अभी उपलब्ध नहीं है",
    nsqf_expired_only: "इस आजीविका के लिए एक पुराना NSQF रिकॉर्ड मौजूद है, लेकिन उसकी दर्ज वैधता अवधि समाप्त हो चुकी है, इसलिए उसे वर्तमान मार्गदर्शन के रूप में नहीं दिखाया जाता।",
    no_scheme: "संबंधित योजना की जानकारी उपलब्ध नहीं है",
    no_opportunity: "सत्यापित स्थानीय अवसर अभी उपलब्ध नहीं हैं",

    listening: "सुना जा रहा है...",
    you_said: "आपने कहा:",
    voice_error: "आवाज़ त्रुटि:",
    speak_first: "पहले बोलें।",
    speech_not_supported: "इस ब्राउज़र में आवाज़ पहचान उपलब्ध नहीं है।",

    enter_beneficiary_id: "पहले लाभार्थी आईडी दर्ज करें।",
    beneficiary_not_found: "लाभार्थी नहीं मिला।",
    recommendation_failed: "आजीविका सुझाव तैयार नहीं किए जा सके।",
    assistant_failed: "जीविका आपके अनुरोध को पूरा नहीं कर सका।",

    loading: "लोड हो रहा है...",
    change_language: "भाषा",

    new_profile: "नई प्रोफ़ाइल",
    show_navigation: "नेविगेशन दिखाएँ",
    hide_navigation: "नेविगेशन छिपाएँ",
    onboarding_manual_mode: "जानकारी भरें",
    onboarding_voice_mode: "आवाज़ से जीविका को बताएँ",
    voice_onboarding_title: "आवाज़ से प्रोफ़ाइल बनाएँ",
    voice_onboarding_subtitle: "जीविका एक-एक करके प्रश्न पूछेगा। अपनी चुनी हुई भाषा में स्वाभाविक रूप से उत्तर दें।",
    voice_start: "वॉइस सेटअप शुरू करें",
    voice_retry: "फिर से बोलें",
    voice_confirm_next: "सही है, आगे बढ़ें",
    voice_skip: "छोड़ें",
    voice_answer_heard: "मैंने सुना:",
    voice_waiting_answer: "तैयार होने पर ‘वॉइस सेटअप शुरू करें’ दबाएँ।",
    voice_question_progress: "प्रश्न {current} / {total}",
    voice_listening_now: "आपका उत्तर सुना जा रहा है...",
    voice_processing: "आपका उत्तर जाँचा जा रहा है...",
    voice_prompting: "जीविका प्रश्न पूछ रहा है...",
    voice_interview_complete: "आपकी प्रोफ़ाइल की जानकारी तैयार है",
    voice_interview_complete_help: "दर्ज जानकारी की समीक्षा करें या प्रोफ़ाइल बनाकर सुझाव प्राप्त करें।",
    voice_create_profile: "प्रोफ़ाइल बनाएँ और सुझाव देखें",
    voice_edit_manually: "जानकारी जाँचें / बदलें",
    voice_unrecognized: "आपका उत्तर स्पष्ट रूप से समझ नहीं आया। कृपया फिर से बोलें।",
    voice_invalid_choice: "आपका उत्तर उपलब्ध विकल्पों से मेल नहीं खा सका। कृपया फिर से बोलें।",
    voice_number_not_understood: "संख्या समझ नहीं आई। कृपया संख्या धीरे से फिर बोलें।",
    voice_microphone_denied: "माइक्रोफ़ोन की अनुमति बंद है। ब्राउज़र में माइक्रोफ़ोन की अनुमति दें या फ़ॉर्म का उपयोग करें।",
    voice_not_supported: "इस ब्राउज़र में वॉइस इनपुट उपलब्ध नहीं है। कृपया फ़ॉर्म का उपयोग करें।",
    voice_optional_hint: "यह प्रश्न वैकल्पिक है। आप ‘छोड़ें’ कह सकते हैं।",
    voice_review_title: "दर्ज की गई प्रोफ़ाइल",
    voice_review_note: "इन जानकारियों का उपयोग आपकी लाभार्थी प्रोफ़ाइल बनाने के लिए किया जाएगा।",
    voice_complete_badge: "तैयार",
    voice_skip_word: "छोड़ें",

    vq_name: "आपका पूरा नाम क्या है?",
    vq_age: "आपकी उम्र कितनी है? कृपया अपनी उम्र संख्या में बोलें।",
    vq_gender: "आपका लिंग क्या है? पुरुष, महिला या अन्य बोलें।",
    vq_state: "आप किस राज्य में रहते हैं?",
    vq_district: "आप किस जिले में रहते हैं?",
    vq_village: "आपके गाँव या शहर का नाम क्या है? यदि नहीं बताना चाहते तो ‘छोड़ें’ कहें।",
    vq_education: "आपने सबसे अधिक कौन-सी शिक्षा पूरी की है? उदाहरण के लिए 10वीं, 12वीं, आईटीआई, डिप्लोमा, स्नातक या औपचारिक शिक्षा नहीं।",
    vq_occupation: "आप अभी क्या काम करते हैं? यदि अभी काम नहीं करते तो ‘काम नहीं करता’ कहें।",
    vq_experience: "आपके पास कितने वर्षों का काम का अनुभव है?",
    vq_skills: "आपके पास कौन-कौन से कौशल हैं? आप एक से अधिक कौशल बता सकते हैं।",
    vq_interests: "आप किस प्रकार के काम में रुचि रखते हैं? आप एक से अधिक रुचियाँ बता सकते हैं।",
    vq_income: "आप हर महीने कितनी आय कमाना चाहते हैं? यदि निश्चित नहीं हैं तो शून्य कह सकते हैं।",
    vq_relocation: "क्या आप काम या प्रशिक्षण के लिए दूसरी जगह जाने के लिए तैयार हैं? हाँ या नहीं कहें।",
    onboarding_title: "आपकी प्रोफ़ाइल बनाते हैं",
    onboarding_subtitle: "उपयुक्त आजीविका मार्ग सुझाने के लिए कुछ सरल प्रश्नों के उत्तर दें।",
    onboarding_step: "चरण {current} / {total}",
    step_personal: "मूल जानकारी",
    step_background: "शिक्षा और काम",
    step_skills: "कौशल और रुचियाँ",
    step_goals: "लक्ष्य और प्राथमिकताएँ",
    full_name: "पूरा नाम",
    age: "आयु",
    gender: "लिंग",
    select_gender: "लिंग चुनें",
    male: "पुरुष",
    female: "महिला",
    other: "अन्य",
    state: "राज्य",
    district: "जिला",
    village: "गाँव / शहर",
    optional: "वैकल्पिक",
    education_level: "उच्चतम शिक्षा",
    select_education: "शिक्षा स्तर चुनें",
    edu_no_school: "औपचारिक शिक्षा नहीं",
    edu_primary: "प्राथमिक विद्यालय",
    edu_8th: "8वीं कक्षा",
    edu_10th: "10वीं कक्षा",
    edu_12th: "12वीं कक्षा",
    edu_iti: "आईटीआई",
    edu_diploma: "डिप्लोमा",
    edu_graduate: "स्नातक",
    edu_postgraduate: "स्नातकोत्तर",
    current_occupation_field: "वर्तमान व्यवसाय",
    occupation_placeholder: "उदाहरण: दोपहिया वाहन मैकेनिक",
    experience_years_field: "कार्य अनुभव (वर्ष)",
    existing_skills_field: "मौजूदा कौशल",
    skills_help: "कौशल को कॉमा से अलग करके लिखें।",
    skills_placeholder: "उदाहरण: वाहन मरम्मत, विद्युत कार्य, उपकरण संचालन",
    interests_field: "काम की रुचियाँ",
    interests_help: "रुचियों को कॉमा से अलग करके लिखें।",
    interests_placeholder: "उदाहरण: ऑटोमोबाइल सर्विसिंग, यांत्रिक कार्य",
    income_target_field: "मासिक आय लक्ष्य",
    income_target_help: "लगभग राशि रुपये में दर्ज करें। यदि निश्चित नहीं हैं तो 0 रहने दें।",
    relocation_field: "क्या आप काम या प्रशिक्षण के लिए स्थान बदलने के इच्छुक हैं?",
    relocate_no: "नहीं",
    relocate_yes: "हाँ",
    back: "पीछे",
    continue_button: "आगे बढ़ें",
    create_profile: "प्रोफ़ाइल बनाएँ और सुझाव देखें",
    creating_profile: "आपकी प्रोफ़ाइल बनाई जा रही है...",
    profile_create_failed: "प्रोफ़ाइल नहीं बन सकी। कृपया जानकारी जाँचकर फिर प्रयास करें।",
    profile_created: "प्रोफ़ाइल सफलतापूर्वक बन गई। सुझाव तैयार किए जा रहे हैं...",
    required_fields: "आगे बढ़ने से पहले सभी आवश्यक जानकारी पूरी करें।",
    skills_required: "कम से कम एक मौजूदा कौशल दर्ज करें।",
    interests_required: "कम से कम एक कार्य रुचि दर्ज करें।",
    invalid_age: "कृपया 18 से 100 के बीच मान्य आयु दर्ज करें।",
    invalid_name: "अक्षरों का उपयोग करके वास्तविक नाम दर्ज करें; यादृच्छिक अक्षर या संख्या न लिखें।",
    invalid_state: "मान्य राज्य का नाम दर्ज करें।",
    invalid_district: "मान्य ज़िले का नाम दर्ज करें।",
    invalid_village: "मान्य गाँव या शहर का नाम दर्ज करें, या इसे खाली छोड़ दें।",
    invalid_occupation: "सार्थक वर्तमान व्यवसाय दर्ज करें, या यदि काम नहीं करते हैं तो इसे खाली छोड़ दें।",
    invalid_experience: "कार्य अनुभव के वर्षों के लिए मान्य संख्या दर्ज करें।",
    experience_age_mismatch: "इस आयु के लिए अनुभव बहुत अधिक लगता है। यहाँ अधिकतम उचित मान {max} वर्ष है।",
    invalid_income: "मासिक आय लक्ष्य ₹0 से ₹10,00,000 के बीच दर्ज करें।",
    invalid_skill_item: "‘{item}’ सार्थक कौशल नहीं लगता। वाहन मरम्मत, वेल्डिंग, सिलाई या उपकरण संचालन जैसे स्पष्ट कौशल लिखें।",
    invalid_interest_item: "‘{item}’ सार्थक कार्य रुचि नहीं लगती। ऑटोमोबाइल सर्विसिंग, विद्युत कार्य, सिलाई या कृषि जैसी स्पष्ट रुचियाँ लिखें।",
    too_many_skills: "कौशल सूची को 12 स्पष्ट कौशल या उससे कम रखें।",
    too_many_interests: "रुचियों की सूची को 12 स्पष्ट रुचियों या उससे कम रखें।",
    profile_fix_errors: "आगे बढ़ने से पहले हाइलाइट किए गए विवरण सुधारें।",
    voice_meaningful_text_needed: "मैं उत्तर को स्पष्ट रूप से नहीं समझ पाया। कृपया साफ़ शब्दों में दोबारा बोलें।",
    no_recommendations_title: "जीविका को थोड़ी और प्रोफ़ाइल जानकारी चाहिए",
    no_recommendations_help: "वर्तमान जानकारी से भरोसेमंद आजीविका मिलान नहीं मिला। इसका अर्थ यह नहीं है कि आपके लिए उपयुक्त आजीविका नहीं है।",
    no_recommendations_tip_skills: "बहुत सामान्य या यादृच्छिक शब्दों की जगह स्पष्ट व्यावहारिक कौशल जोड़ें।",
    no_recommendations_tip_interests: "वह काम जोड़ें जिसे आप वास्तव में करना चाहते हैं।",
    no_recommendations_tip_occupation: "यदि हो तो अपना वर्तमान या पिछला व्यवसाय जोड़ें।",
    low_confidence_title: "प्रारंभिक मिलान:",
    low_confidence_help: "उपलब्ध प्रोफ़ाइल मिलान अपेक्षाकृत कमजोर है। इन्हें मजबूत सुझाव मानने से पहले अधिक स्पष्ट कौशल और रुचियाँ जोड़ें।",
    new_profile_confirm: "नई प्रोफ़ाइल शुरू करें? इस ब्राउज़र की वर्तमान प्रोफ़ाइल साफ़ हो जाएगी।",
    dashboard_loading: "आपके व्यक्तिगत सुझाव तैयार किए जा रहे हैं...",

    recommendation_reason:
      "{occupation} आपकी जानकारी के आधार पर सुझाया गया है। मिलते हुए कौशल: {skills}. वर्तमान सुझाव प्रणाली के अनुसार कुल प्रोफ़ाइल मेल: {score}%.",

    no_matched_skills_for_reason: "प्रोफ़ाइल कारक"
  }
};


const dynamicTranslations = {
  kn: {
    "10th": "10ನೇ ತರಗತಿ",
    "12th": "12ನೇ ತರಗತಿ",
    "Graduate": "ಪದವಿ",
    "No formal schooling": "ಔಪಚಾರಿಕ ಶಿಕ್ಷಣ ಇಲ್ಲ",
    "Primary": "ಪ್ರಾಥಮಿಕ ಶಾಲೆ",
    "8th": "8ನೇ ತರಗತಿ",
    "ITI": "ಐಟಿಐ",
    "Diploma": "ಡಿಪ್ಲೊಮಾ",
    "Postgraduate": "ಸ್ನಾತಕೋತ್ತರ",
    "Male": "ಪುರುಷ",
    "Female": "ಮಹಿಳೆ",
    "Other": "ಇತರೆ",
    "Not working": "ಪ್ರಸ್ತುತ ಕೆಲಸದಲ್ಲಿಲ್ಲ",

    "Automotive": "ವಾಹನ ಕ್ಷೇತ್ರ",
    "Electrical": "ವಿದ್ಯುತ್ ಕ್ಷೇತ್ರ",
    "Repair and Maintenance": "ದುರಸ್ತಿ ಮತ್ತು ನಿರ್ವಹಣೆ",

    "Two-Wheeler Mechanic": "ದ್ವಿಚಕ್ರ ವಾಹನ ಮೆಕ್ಯಾನಿಕ್",
    "Four-Wheeler Mechanic (Light Motor Vehicle)": "ನಾಲ್ಕು ಚಕ್ರ ವಾಹನ ಮೆಕ್ಯಾನಿಕ್ (ಲಘು ಮೋಟಾರು ವಾಹನ)",
    "AC and Refrigeration Repair Technician": "ಎಸಿ ಮತ್ತು ಶೀತಲೀಕರಣ ದುರಸ್ತಿ ತಂತ್ರಜ್ಞ",
    "Generator/DG Set Mechanic": "ಜನರೇಟರ್ / ಡಿಜಿ ಸೆಟ್ ಮೆಕ್ಯಾನಿಕ್",
    "Electrical Wireman": "ವಿದ್ಯುತ್ ವೈರ್‌ಮನ್",

    "Two Wheeler Service Technician": "ದ್ವಿಚಕ್ರ ವಾಹನ ಸೇವಾ ತಂತ್ರಜ್ಞ",
    "Four Wheeler Service Technician": "ನಾಲ್ಕು ಚಕ್ರ ವಾಹನ ಸೇವಾ ತಂತ್ರಜ್ಞ",

    "vehicle repair": "ವಾಹನ ದುರಸ್ತಿ",
    "basic electrical work": "ಮೂಲಭೂತ ವಿದ್ಯುತ್ ಕೆಲಸ",
    "tool handling": "ಉಪಕರಣ ಬಳಕೆ",
    "electrical work": "ವಿದ್ಯುತ್ ಕೆಲಸ",
    "mechanical work": "ಯಾಂತ್ರಿಕ ಕೆಲಸ",
    "diagnostics": "ದೋಷ ಪತ್ತೆ",
    "tools": "ಉಪಕರಣಗಳು",
    "automobiles": "ವಾಹನಗಳು",
    "wiring": "ವೈರಿಂಗ್",

    "automobile servicing": "ವಾಹನ ಸರ್ವಿಸಿಂಗ್",
    "technical skills": "ತಾಂತ್ರಿಕ ಕೌಶಲ್ಯಗಳು",

    "training and certification": "ತರಬೇತಿ ಮತ್ತು ಪ್ರಮಾಣೀಕರಣ",

    "apprenticeship training and stipend-related support under applicable rules":
      "ಅನ್ವಯಿಸುವ ನಿಯಮಗಳಡಿ ಅಪ್ರೆಂಟಿಸ್ ತರಬೇತಿ ಮತ್ತು ಭತ್ಯೆ ಸಂಬಂಧಿತ ಬೆಂಬಲ",

    "credit-linked subsidy and enterprise finance":
      "ಸಾಲಕ್ಕೆ ಸಂಬಂಧಿಸಿದ ಸಹಾಯಧನ ಮತ್ತು ಉದ್ಯಮ ಹಣಕಾಸು",

    "skill training and placement-linked support":
      "ಕೌಶಲ್ಯ ತರಬೇತಿ ಮತ್ತು ಉದ್ಯೋಗ ಸಂಪರ್ಕಿತ ಬೆಂಬಲ"
  },

  hi: {
    "10th": "10वीं कक्षा",
    "12th": "12वीं कक्षा",
    "Graduate": "स्नातक",
    "No formal schooling": "औपचारिक शिक्षा नहीं",
    "Primary": "प्राथमिक विद्यालय",
    "8th": "8वीं कक्षा",
    "ITI": "आईटीआई",
    "Diploma": "डिप्लोमा",
    "Postgraduate": "स्नातकोत्तर",
    "Male": "पुरुष",
    "Female": "महिला",
    "Other": "अन्य",
    "Not working": "वर्तमान में काम नहीं कर रहे",

    "Automotive": "ऑटोमोबाइल",
    "Electrical": "विद्युत",
    "Repair and Maintenance": "मरम्मत और रखरखाव",

    "Two-Wheeler Mechanic": "दोपहिया वाहन मैकेनिक",
    "Four-Wheeler Mechanic (Light Motor Vehicle)": "चार-पहिया वाहन मैकेनिक (हल्का मोटर वाहन)",
    "AC and Refrigeration Repair Technician": "एसी और रेफ्रिजरेशन मरम्मत तकनीशियन",
    "Generator/DG Set Mechanic": "जनरेटर / डीजी सेट मैकेनिक",
    "Electrical Wireman": "इलेक्ट्रिकल वायरमैन",

    "Two Wheeler Service Technician": "दोपहिया सेवा तकनीशियन",
    "Four Wheeler Service Technician": "चार-पहिया सेवा तकनीशियन",

    "vehicle repair": "वाहन मरम्मत",
    "basic electrical work": "मूल विद्युत कार्य",
    "tool handling": "उपकरण संचालन",
    "electrical work": "विद्युत कार्य",
    "mechanical work": "यांत्रिक कार्य",
    "diagnostics": "दोष पहचान",
    "tools": "उपकरण",
    "automobiles": "वाहन",
    "wiring": "वायरिंग",

    "automobile servicing": "ऑटोमोबाइल सर्विसिंग",
    "technical skills": "तकनीकी कौशल",

    "training and certification": "प्रशिक्षण और प्रमाणन",

    "apprenticeship training and stipend-related support under applicable rules":
      "लागू नियमों के तहत अप्रेंटिसशिप प्रशिक्षण और वजीफा संबंधी सहायता",

    "credit-linked subsidy and enterprise finance":
      "ऋण-संबंधित सब्सिडी और उद्यम वित्त",

    "skill training and placement-linked support":
      "कौशल प्रशिक्षण और प्लेसमेंट-संबंधित सहायता"
  }
};


let currentLanguage =
  localStorage.getItem("jeevikaLanguage") || "en";


function t(key) {
  return (
    translations[currentLanguage]?.[key] ||
    translations.en[key] ||
    key
  );
}


function formatT(key, values = {}) {

  let text = t(key);

  Object.entries(values).forEach(
    ([name, value]) => {

      text = text.replaceAll(
        `{${name}}`,
        value
      );

    }
  );

  return text;
}


function translateValue(value) {

  if (
    value === null ||
    value === undefined ||
    value === ""
  ) {
    return "";
  }

  if (currentLanguage === "en") {
    return String(value);
  }

  return (
    dynamicTranslations[currentLanguage]?.[
      String(value)
    ] ||
    String(value)
  );
}


function getLanguageConfig() {
  return JEEVIKA_LANGUAGES[currentLanguage];
}


function getBackendLanguage() {
  return getLanguageConfig().backendName;
}


function getSpeechLocale() {
  return getLanguageConfig().speech;
}


function applyLanguage(lang) {

  if (!JEEVIKA_LANGUAGES[lang]) {
    lang = "en";
  }

  currentLanguage = lang;

  localStorage.setItem(
    "jeevikaLanguage",
    lang
  );

  document.documentElement.lang =
    JEEVIKA_LANGUAGES[lang].htmlLang;

  document.title =
    t("page_title");


  document
    .querySelectorAll("[data-i18n]")
    .forEach(element => {

      const key =
        element.getAttribute("data-i18n");

      element.textContent =
        t(key);

    });


  document
    .querySelectorAll("[data-i18n-placeholder]")
    .forEach(element => {

      const key =
        element.getAttribute(
          "data-i18n-placeholder"
        );

      element.placeholder =
        t(key);

    });


  document
    .querySelectorAll("[data-i18n-aria-label]")
    .forEach(element => {

      const key =
        element.getAttribute(
          "data-i18n-aria-label"
        );

      element.setAttribute(
        "aria-label",
        t(key)
      );

    });


  const languageSelect =
    document.getElementById("language");

  if (languageSelect) {

    languageSelect.value =
      getBackendLanguage();

  }


  window.dispatchEvent(
    new CustomEvent(
      "jeevika-language-changed",
      {
        detail: {
          language: lang
        }
      }
    )
  );
}


function selectJeevikaLanguage(lang) {

  applyLanguage(lang);

  const gate =
    document.getElementById("languageGate");

  if (gate) {
    gate.classList.add(
      "language-gate-hidden"
    );
  }
}


function showLanguageGate() {

  const gate =
    document.getElementById("languageGate");

  if (gate) {
    gate.classList.remove(
      "language-gate-hidden"
    );
  }
}


document.addEventListener(
  "DOMContentLoaded",
  () => {

    const savedLanguage =
      localStorage.getItem(
        "jeevikaLanguage"
      );

    if (savedLanguage) {

      currentLanguage =
        JEEVIKA_LANGUAGES[savedLanguage]
          ? savedLanguage
          : "en";

      applyLanguage(
        currentLanguage
      );

    }
    else {

      currentLanguage = "en";

      document.documentElement.lang =
        "en";

      document.title =
        translations.en.page_title;

      document
        .querySelectorAll(
          "[data-i18n]"
        )
        .forEach(element => {

          const key =
            element.getAttribute(
              "data-i18n"
            );

          element.textContent =
            translations.en[key] ||
            key;

        });

      document
        .querySelectorAll(
          "[data-i18n-placeholder]"
        )
        .forEach(element => {

          const key =
            element.getAttribute(
              "data-i18n-placeholder"
            );

          element.placeholder =
            translations.en[key] ||
            key;

        });

      showLanguageGate();

    }

  }
);